from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from users.models import User

from backend.settings import SECRET_KEY

import jwt
import datetime


class JWTAuthentication(BaseAuthentication):

  def authenticate(self, request):
      token = request.COOKIES.get("refresh")

      if not token:
        return None

      try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
      except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed("unauthenticated")

      user = User.objects.get(pk=payload["user_id"])
      if user is None:
        raise exceptions.AuthenticationFailed("User not found")

      return (user, None)

  @staticmethod
  def generate_jwt(id: int, scope: str):
    payload = {
      "user_id": id,
      "scope": scope,
      "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30),
      "iat": datetime.datetime.utcnow()
    }

    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

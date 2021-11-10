from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from users.models import User

from rest_framework_simplejwt.tokens import RefreshToken

from backend.settings import SECRET_KEY

import jwt

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def verify_jwt_token(refresh_token: str):
  try:
    payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=["HS256"])
  except jwt.ExpiredSignatureError:
    return None

  return payload

class JWTAuthentication(BaseAuthentication):

  def authenticate(self, request):
      print()

      if not "Authorization" in request.headers:
        raise exceptions.AuthenticationFailed("Please proveide access token")

      # token = request.COOKIES.get("jwt")
      print(request.headers["Authorization"].split()[1])
      token = request.headers["Authorization"].split()[1]

      if not token:
        return None

      try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
      except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed("unauthenticated")

      user = User.objects.get(pk=payload["user_id"])

      print(user)

      if user is None:
        raise exceptions.AuthenticationFailed("User not found")

      return (user, None)

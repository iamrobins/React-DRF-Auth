from rest_framework import exceptions
from rest_framework.views import APIView

from users.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from .authentication import get_tokens_for_user, verify_jwt_token, JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication

class RegisterAPIView(APIView):

  def post(self, request):
    data = request.data
    if data["password"] != data["password_confirm"]:
      raise exceptions.AuthenticationFailed("Password confirm does not match")

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)




class LoginAPIView(APIView):

  def get(self, request):
    print(request.user)
    return Response("login hi")

  def post(self, request):
    email = request.data["email"]
    password = request.data["password"]

    user = User.objects.filter(email=email).first()

    if user is None:
      raise exceptions.AuthenticationFailed("Email not registered")

    if not user.check_password(password):
      raise exceptions.AuthenticationFailed("Incorrect Password")

    token = get_tokens_for_user(user)

    response = Response()

    response.set_cookie("refresh", token["refresh"], httponly=True)
    response.data = {"access_token": token["access"]}

    return response


class ProfileAPIView(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]

  def get(self, request):
    user = User.objects.filter(email=request.user).first()

    if user is None:
      raise exceptions.APIException("User not found")

    return Response(UserSerializer(user).data)

class RefreshTokenObtainView(APIView):

  def get(self, request):
    refresh_token = request.COOKIES.get("refresh")
    payload = verify_jwt_token(refresh_token)

    if payload is None:
      raise exceptions.AuthenticationFailed("Refresh Token Expire/Invalid")

    user = User.objects.get(pk=payload["user_id"])

    if user is None:
        raise exceptions.AuthenticationFailed("User not found")

    token = get_tokens_for_user(user)
    response = Response()
    response.set_cookie("refresh", token["refresh"], httponly=True)
    response.data = {"access_token": token["access"]}

    return response
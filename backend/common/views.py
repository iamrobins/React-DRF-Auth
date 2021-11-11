from rest_framework import exceptions
from rest_framework.views import APIView

from users.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from .authentication import JWTAuthentication
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
    return Response("login hi GET route")

  def post(self, request):
    email = request.data["email"]
    password = request.data["password"]

    user = User.objects.filter(email=email).first()

    if user is None:
      raise exceptions.AuthenticationFailed("Email not registered")

    if not user.check_password(password):
      raise exceptions.AuthenticationFailed("Incorrect Password")

    scope = "admin"

    if "api/admin/" not in request.path:
      scope = "user"

    token = JWTAuthentication.generate_jwt(user.id, scope)

    response = Response()

    response.set_cookie("refresh", token, httponly=True)
    response.data = {"message": "success"}

    return response

class LogoutAPIView(APIView):

  def get(self, _):
    response = Response()
    response.delete_cookie("refresh")
    response.data = {"message": "success"}
    return response


class ProfileAPIView(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]

  def get(self, request):
    user = User.objects.filter(email=request.user).first()

    if user is None:
      raise exceptions.APIException("User not found")

    return Response(UserSerializer(user).data)
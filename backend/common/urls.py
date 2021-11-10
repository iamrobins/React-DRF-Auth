from django.urls import path
from .views import RegisterAPIView, LoginAPIView, ProfileAPIView, MyRefreshToken


urlpatterns = [
  path("register/", RegisterAPIView.as_view(), name="register"),
  path("login/", LoginAPIView.as_view(), name="login"),
  path('user/', ProfileAPIView.as_view(), name='profile'),
  path('token/refresh/', MyRefreshToken.as_view(), name='my_token_refresh'),
]
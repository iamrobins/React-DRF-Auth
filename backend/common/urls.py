from django.urls import path
from .views import RegisterAPIView, LoginAPIView, ProfileAPIView, RefreshTokenObtainView


urlpatterns = [
  path("register/", RegisterAPIView.as_view(), name="register"),
  path("login/", LoginAPIView.as_view(), name="login"),
  path('user/', ProfileAPIView.as_view(), name='profile'),
  path('token/refresh/', RefreshTokenObtainView.as_view(), name='token_refresh'),
]
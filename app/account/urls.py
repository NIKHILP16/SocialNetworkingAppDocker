from django.shortcuts import render

# Create your views here.
from django.urls import path
from .views import RegistrationView, LoginView, LogoutView,ChangePasswordView
from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='register'),
    path('change-password', ChangePasswordView.as_view(), name='register'),
    path('token-refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
from django.shortcuts import render

# Create your views here.
from django.urls import path
from .views import ProfileView
from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    path('get_profiles', ProfileView.as_view({'get': 'get_profiles'})),
]
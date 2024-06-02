from django.shortcuts import render

# Create your views here.
from django.urls import path
from .views import ProfileView, FriendRequest
from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    path('profile/<uuid:profile_id>', ProfileView.as_view({'get': 'get_profiles'})),
    path('find_friends', ProfileView.as_view({'get': 'get_profiles'})),
    path('friend_list', ProfileView.as_view({'get': 'friend_list'})),
    path('send_request/<uuid:profile_id>', FriendRequest.as_view({'post': 'send_friend_request'})),
    path('pending_request', FriendRequest.as_view({'get': 'pending_request'})),
    path('accept_request/<uuid:friend_request_id>', FriendRequest.as_view({'post': 'accept_friend_request'})),
    path('reject_request/<uuid:friend_request_id>', FriendRequest.as_view({'post': 'reject_friend_request'})),
    ]   
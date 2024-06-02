from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import authentication
from rest_framework.response import  Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework import generics, status
from .serializers import ProfileSerializer,FriendRequestSerializer
from .models import Profile,FriendRequests
from .utils import CustomValidation
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
# Create your views here.

class ProfileView(GenericViewSet):
    permission_classes = [IsAuthenticated, ]
    authentication_classes=[authentication.JWTAuthentication]
    pagination_class = PageNumberPagination
    def get_profiles(self,request,profile_id=None,*args, **kwargs):
        try:
            profile_id = profile_id or request.query_params.get('profile_id')
            if profile_id:
                profile=Profile.objects.filter(user=request.user,id=profile_id).first()
                profile_serializer = ProfileSerializer(profile)
                return Response(profile_serializer.data, status=status.HTTP_200_OK)   
            else:
                search = request.GET.get('search')
                profile_list=[]     
                if search:
                    profile_list=Profile.objects.filter( Q(user__email__iexact=search) )
                    if not profile_list:
                        profile_list=Profile.objects.filter( Q(user__name__icontains=search) )

                else:
                    profile_list=Profile.objects.all()
                paginator = self.pagination_class()
                result_page = paginator.paginate_queryset(profile_list, request) 
                serializer = ProfileSerializer(result_page, many=True)
                return paginator.get_paginated_response(serializer.data) 
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def friend_list(self,request):
        friend_list=Profile.objects.get(user=request.user).friends.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(friend_list, request) 
        serializer = ProfileSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data) 



class FriendRequest(GenericViewSet):
    permission_classes = [IsAuthenticated, ]
    authentication_classes=[authentication.JWTAuthentication]

    @method_decorator(ratelimit(key='ip', rate='3/m', method='POST'))
    def send_friend_request(self,request, profile_id=None,*args, **kwargs):
        try:
            sender_user_profile = Profile.objects.get(user=request.user)
            reciver_user_profile = Profile.objects.get(id=profile_id)
            check = FriendRequests.objects.filter(receiver=reciver_user_profile).filter(sender=sender_user_profile).values('status')
            if not check:
                friendrequest = FriendRequests.objects.create(receiver=reciver_user_profile, sender=sender_user_profile)
                return Response({'message': 'friendship request send',
                                'id':friendrequest.id},status=status.HTTP_200_OK)
            elif check[0].get('status')=="accepted":
                return Response({'message': 'Already Friend'},status=status.HTTP_200_OK)
            else:
                return Response({'message': 'request already sent'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Invalid profile id'},status=status.HTTP_400_BAD_REQUEST)

    
    def pending_request(self,request, *args, **kwargs):
        request_list=[]
        try:
            request_list=FriendRequests.objects.filter(receiver=Profile.objects.get(user=request.user),status="send")
            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(request_list, request) 
            serializer = FriendRequestSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)    
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def accept_friend_request(self,request,friend_request_id=None, *args, **kwargs):    
        serializer = FriendRequestSerializer(data=request.data,context={'friend_request_id': friend_request_id},partial=True)
        if serializer.is_valid():
            serializer.accept_request()
            return Response( status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def reject_friend_request(self,request,friend_request_id=None, *args, **kwargs):    
        serializer = FriendRequestSerializer(data=request.data,context={'friend_request_id': friend_request_id},partial=True)
        if serializer.is_valid():
            serializer.reject_request()
            return Response( status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
             
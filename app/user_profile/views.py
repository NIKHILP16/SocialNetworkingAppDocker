from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import  Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework import generics, status
from .serializers import ProfileSerializer
from .models import Profile
# Create your views here.

class ProfileView(GenericViewSet):
    permission_classes = [IsAuthenticated, ]
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
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

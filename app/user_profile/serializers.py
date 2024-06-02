from rest_framework import serializers
from .models import Profile, FriendRequests
from. utils import CustomValidation
from rest_framework import status

class ProfileSerializer(serializers.ModelSerializer):
    user_name=serializers.ReadOnlyField(source="user.name")
    user_email=serializers.ReadOnlyField(source="user.email")
    
    class Meta:
        model = Profile
        fields = ("id","user_name","user_email","friends_count")
       

class FriendRequestSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = FriendRequests
        fields = ('id', 'status')


    def accept_request(self):
        try:
            obj = FriendRequests.objects.get(id=self.context['friend_request_id'])
            obj.status="accepted"
            obj.save()
            obj.sender.friends.add(obj.sender)
            #Profile.objects.get()
            
        except FriendRequests.DoesNotExist:
            raise CustomValidation("id","Invalid friend request",status_code=status.HTTP_404_NOT_FOUND)
        
    def reject_request(self):
        try:
            obj = FriendRequests.objects.get(id=self.context['friend_request_id'])
            obj.status="rejected"
            obj.save()
        except FriendRequests.DoesNotExist:
            raise CustomValidation("id","Invalid friend request",status_code=status.HTTP_404_NOT_FOUND)
        



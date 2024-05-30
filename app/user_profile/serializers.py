from rest_framework import serializers
from .models import Profile
from rest_framework.exceptions import APIException
from django.utils.encoding import force_str
from rest_framework import status


# ========================= Custum Validation Start ==================================== 

class CustomValidation(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, field,detail,  status_code):
        if status_code is not None:self.status_code = status_code
        if detail is not None:
            self.detail = {field: force_str(detail)}
        else: self.detail = {'detail': force_str(self.default_detail)}

# ========================= Custum Validation End ====================================
class ProfileSerializer(serializers.ModelSerializer):
    user_name=serializers.ReadOnlyField(source="user.name")
    user_email=serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Profile
        #exclude = ('user','last_modified','invoice_json' )
        fields = ("user","user_name","user_email")


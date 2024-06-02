from rest_framework import serializers
from .models import User as MyUser
from rest_framework.exceptions import APIException
from django.utils.encoding import force_str
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


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

class RegistrationSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(required=True,allow_blank=False, allow_null=False)
    password = serializers.CharField(required=True,allow_blank=False, allow_null=False)
    name = serializers.CharField(required=True,allow_blank=False, allow_null=False)
    class Meta:
        model = MyUser
        fields = ['email', 'password','name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = MyUser(email=(self.validated_data['email']).lower())
        password = self.validated_data['password']
        name = (self.validated_data['name']).capitalize()      
        if MyUser.objects.filter(email = self.validated_data['email']).exists():
            raise CustomValidation("email","Email already exist",status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        user.name = name
        user.set_password(password)
        user.save()
        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise CustomValidation("current_password","Old password does not match",status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
        return value
    


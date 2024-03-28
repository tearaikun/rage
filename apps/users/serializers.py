from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apps.users.models import User, ConfirmCode


class UserSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = [
            'id',
            "username",
            'first_name',
            "last_name",
            'age',
            'job',
            'email',
            'phone_number',
            "password",
            "is_active"
        ]

        read_only_fields = (
            "id",
            "is_active",
        )


class ConfirmCodeSerializer(ModelSerializer):
    class Meta:
        model = ConfirmCode
        fields = [
            'id',
            "user",
            "token"
        ]        
    


    def create(self, validated_data: dict):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password) 
        user.is_active = False
        user.save()
        return user
    

class ConfirmCodeSerializer(ModelSerializer):
    class Meta:
        model = ConfirmCode
        fields = [
            "id",
            "user",
            "token"
        ]

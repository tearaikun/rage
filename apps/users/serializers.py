from rest_framework.serializers import ModelSerializer

from apps.users.models import User 

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
        ]
        
    
    def create(self, validated_data: dict):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password) 
        user.is_active = True
        user.save()
        return user

from rest_framework.serializers import ModelSerializer

from apps.users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "fullname",
            "age",
            "job",
            "phone_number",
            "email"
        ]
        
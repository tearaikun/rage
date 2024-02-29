from rest_framework.serializers import ModelSerializer

from apps.contacts.models import Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "id",
            "phone_number",
            "email",
            "instagram",
            "tiktok"
        ]
        
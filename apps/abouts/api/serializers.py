from rest_framework.serializers import ModelSerializer

from apps.abouts.models import About


class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = [
            "id",
            "title",
            "image",
            "description"
        ]
        
from rest_framework.serializers import ModelSerializer

from apps.news.models import New


class NewSerializer(ModelSerializer):
    class Meta:
        model = New
        fields = [
            "id",
            "image",
            "title",
            "description"
        ]
        
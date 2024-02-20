from rest_framework.serializers import ModelSerializer

from apps.rage.models import Rage


class RageSerializer(ModelSerializer):
    class Meta:
        model = Rage
        fields = [
            "id",
            "image",
            "name",
            "job"
        ]
        
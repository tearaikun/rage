from rest_framework.serializers import ModelSerializer

from apps.studies.models import Studies


class StudiesSerializer(ModelSerializer):
    class Meta:
        model = Studies
        fields = [
            "id",
            "title",
            "link"
        ]
        
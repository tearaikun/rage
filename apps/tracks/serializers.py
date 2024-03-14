from rest_framework.serializers import ModelSerializer

from apps.tracks.models import Track


class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = [
            "id",
            "title",
            "image",
            "date",
            "artist"
        ]

        
        

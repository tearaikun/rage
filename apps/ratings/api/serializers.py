from rest_framework.serializers import ModelSerializer

from apps.ratings.models import Rating


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = [
            "id",
            "rating",
            "feedback",
            "author"
        ]
        
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status


from apps.ratings.models import Rating
from apps.ratings.serializers import RatingSerializer
from apps.tracks.models import Track


class RatingApiViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filterset_fields = [
        'author', 
        "track"
    ]
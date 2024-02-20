from rest_framework.viewsets import ModelViewSet

from apps.ratings.models import Rating
from apps.ratings.api.serializers import RatingSerializer


class RatingApiViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
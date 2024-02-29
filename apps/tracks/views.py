from rest_framework.viewsets import ModelViewSet

from apps.tracks.models import Track
from apps.tracks.serializers import TrackSerializer


class TrackApiViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
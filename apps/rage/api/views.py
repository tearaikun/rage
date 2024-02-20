from rest_framework.viewsets import ModelViewSet

from apps.rage.models import Rage
from apps.rage.api.serializers import RageSerializer


class RageApiViewSet(ModelViewSet):
    queryset = Rage.objects.all()
    serializer_class = RageSerializer
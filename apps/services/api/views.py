from rest_framework.viewsets import ModelViewSet

from apps.services.models import Service
from apps.services.api.serializers import ServiceSerializer


class ServiceApiViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
from rest_framework.viewsets import ModelViewSet

from apps.abouts.models import About
from apps.abouts.api.serializers import AboutSerializer


class AboutApiViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
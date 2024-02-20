from rest_framework.viewsets import ModelViewSet

from apps.studies.models import Studies
from apps.studies.api.serializers import StudiesSerializer


class StudiesApiViewSet(ModelViewSet):
    queryset = Studies.objects.all()
    serializer_class = StudiesSerializer
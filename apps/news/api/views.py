from rest_framework.viewsets import ModelViewSet

from apps.news.models import New
from apps.news.api.serializers import NewSerializer


class NewApiViewSet(ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    
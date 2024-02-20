from rest_framework.viewsets import ModelViewSet

from apps.users.models import User
from apps.users.api.serializers import UserSerializer


class UserApiViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
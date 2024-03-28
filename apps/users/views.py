from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.serializers import UserSerializer, ConfirmCodeSerializer
from apps.users.models import User, ConfirmCode

class UserApiViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class ConfirmCodeApiViewSet(ModelViewSet):
    queryset = ConfirmCode.objects.all()
    serializer_class = ConfirmCodeSerializer


class ActivationApiView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        print(dir(request.query_params))
        token = request.query_params.get("token")
        if token is not None:
            confirm_code = ConfirmCode.objects.get(token=token)
            confirm_code.user.is_active = True
            confirm_code.user.save()
            return Response(
                data={
                    "status": "user activated",
                }, status=status.HTTP_200_OK
            )
        return Response(
            data={
                "error": "token is not found"
            }, status=status.HTTP_400_BAD_REQUEST
        )
from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.users.views import UserApiViewSet, ConfirmCodeApiViewSet, ActivationApiView

router = DefaultRouter()
router.register('users', UserApiViewSet)
router.register('confrimcode', ConfirmCodeApiViewSet)

urlpatterns = [
    path("activation_link/", ActivationApiView.as_view())
]

urlpatterns += router.urls

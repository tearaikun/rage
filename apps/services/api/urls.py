from rest_framework.routers import DefaultRouter

from apps.services.api.views import ServiceApiViewSet

router = DefaultRouter()
router.register(
    r'service',
    ServiceApiViewSet
)

urlpatterns = router.urls

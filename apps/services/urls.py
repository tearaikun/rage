from rest_framework.routers import DefaultRouter

from apps.services.views import ServiceApiViewSet

router = DefaultRouter()
router.register(
    r'service',
    ServiceApiViewSet
)

urlpatterns = router.urls

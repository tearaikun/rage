from rest_framework.routers import DefaultRouter

from apps.rage.views import RageApiViewSet

router = DefaultRouter()
router.register(
    r'rage',
    RageApiViewSet
)

urlpatterns = router.urls

from rest_framework.routers import DefaultRouter

from apps.studies.views import StudiesApiViewSet

router = DefaultRouter()
router.register(
    r'studies',
    StudiesApiViewSet
)

urlpatterns = router.urls

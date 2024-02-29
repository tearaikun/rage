from rest_framework.routers import DefaultRouter

from apps.tracks.views import TrackApiViewSet

router = DefaultRouter()
router.register(
    r'track',
    TrackApiViewSet
)

urlpatterns = router.urls

from rest_framework.routers import DefaultRouter

from apps.ratings.api.views import RatingApiViewSet

router = DefaultRouter()
router.register(
    r'rating',
    RatingApiViewSet
)

urlpatterns = router.urls

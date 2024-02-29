from rest_framework.routers import DefaultRouter

from apps.ratings.views import RatingApiViewSet

router = DefaultRouter()
router.register(
    r'rating',
    RatingApiViewSet
)

urlpatterns = router.urls

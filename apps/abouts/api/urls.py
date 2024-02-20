from rest_framework.routers import DefaultRouter

from apps.abouts.api.views import AboutApiViewSet

router = DefaultRouter()
router.register(
    r'abouts',
    AboutApiViewSet
)

urlpatterns = router.urls

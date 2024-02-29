from rest_framework.routers import DefaultRouter

from apps.abouts.views import AboutApiViewSet

router = DefaultRouter()
router.register(
    r'abouts',
    AboutApiViewSet
)

urlpatterns = router.urls

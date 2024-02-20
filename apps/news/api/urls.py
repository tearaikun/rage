from rest_framework.routers import DefaultRouter

from apps.news.api.views import NewApiViewSet

router = DefaultRouter()
router.register(
    r'news',
    NewApiViewSet
)

urlpatterns = router.urls

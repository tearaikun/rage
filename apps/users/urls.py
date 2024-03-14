from rest_framework.routers import DefaultRouter

from apps.users.views import UserApiViewSet

router = DefaultRouter()
router.register(
    r'user',
    UserApiViewSet
)

urlpatterns = router.urls

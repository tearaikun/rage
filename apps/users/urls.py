from rest_framework.routers import DefaultRouter

from apps.users.views import UserApiViewSet

router = DefaultRouter()
router.register(
    r'users',
    UserApiViewSet
)

urlpatterns = router.urls

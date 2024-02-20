from rest_framework.routers import DefaultRouter

from apps.contacts.api.views import ContactApiViewSet

router = DefaultRouter()
router.register(
    r'contacts',
    ContactApiViewSet
)

urlpatterns = router.urls

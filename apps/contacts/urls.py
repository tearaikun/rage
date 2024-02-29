from rest_framework.routers import DefaultRouter

from apps.contacts.views import ContactApiViewSet

router = DefaultRouter()
router.register(
    r'contacts',
    ContactApiViewSet
)

urlpatterns = router.urls

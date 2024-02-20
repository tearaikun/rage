from rest_framework.viewsets import ModelViewSet

from apps.contacts.models import Contact
from apps.contacts.api.serializers import ContactSerializer


class ContactApiViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
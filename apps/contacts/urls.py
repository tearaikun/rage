from django.urls import path

from apps.contacts.views import get_contact

urlpatterns = [
    path("", get_contact, name="main")
]

from django.urls import path

from apps.services.views import get_service

urlpatterns = [
    path("", get_service, name="main")
]

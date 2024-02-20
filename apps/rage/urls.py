from django.urls import path

from apps.rage.views import get_rage

urlpatterns = [
    path("", get_rage, name="main")
]

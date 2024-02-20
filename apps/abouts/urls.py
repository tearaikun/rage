from django.urls import path

from apps.abouts.views import get_about

urlpatterns = [
    path("", get_about, name="main")
]

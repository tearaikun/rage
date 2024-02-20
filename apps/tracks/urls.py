from django.urls import path

from apps.tracks.views import get_track

urlpatterns = [
    path("", get_track, name="main")
]

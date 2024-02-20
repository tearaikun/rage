from django.urls import path

from apps.news.views import get_new

urlpatterns = [
    path("", get_new, name="main")
]

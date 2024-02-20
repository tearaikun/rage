from django.urls import path

from apps.ratings.views import get_rating

urlpatterns = [
    path("", get_rating, name="main")
]

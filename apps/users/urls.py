from django.urls import path

from apps.users.views import get_user

urlpatterns = [
    path("", get_user, name="main")
]

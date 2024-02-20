from django.urls import path

from apps.studies.views import get_studies

urlpatterns = [
    path("", get_studies, name="main")
]

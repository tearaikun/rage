from django.shortcuts import render

from apps.services.models import Service


def get_service(request):
    service = Service.objects.all()
    return render(request,  {'service': service})
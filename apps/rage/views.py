from django.shortcuts import render

from apps.rage.models import Rage


def get_rage(request):
    rage = Rage.objects.all()
    return render(request, {'rage': rage})
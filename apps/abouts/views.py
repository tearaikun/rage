from django.shortcuts import render

from apps.abouts.models import About


def get_about(request):
    about = About.objects.all()
    return render(request,  {'about': about})
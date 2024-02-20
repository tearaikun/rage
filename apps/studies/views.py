from django.shortcuts import render

from apps.studies.models import Studies


def get_studies(request):
    studies = Studies.objects.all()
    return render(request,  {'studies': studies})
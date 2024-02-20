from django.shortcuts import render

from apps.news.models import New


def get_new(request):
    new = New.objects.all()
    return render(request,  {'new': new})
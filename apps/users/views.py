from django.shortcuts import render

from apps.users.models import User


def get_user(request):
    user = User.objects.all()
    return render(request)
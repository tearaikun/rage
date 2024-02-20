from django.shortcuts import render

from apps.ratings.models import Rating


def get_rating(request):
    rating = Rating.objects.all()
    return render(request,  {'rating': rating})
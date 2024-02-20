from django.shortcuts import render

from apps.tracks.models import Track


def get_track(request):
    track = Track.objects.all()
    return render(request,  {'track': track})
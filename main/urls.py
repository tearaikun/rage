
from django.contrib import admin
from django.urls import path, include



api_urlpatterns = [
    path('', include('apps.users.api.urls')),
    path('', include('apps.abouts.api.urls')),
    path('', include('apps.tracks.api.urls')),
    path('', include('apps.ratings.api.urls')),
    path('', include('apps.studies.api.urls')),
    path('', include('apps.rage.api.urls')),
    path('', include('apps.contacts.api.urls')),
    path('', include('apps.services.api.urls')),
    path('', include('apps.news.api.urls')),
    path('', include('apps.services.api.urls')),
]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
    path('', include('apps.users.urls')),
    path("tracks/", include("apps.tracks.urls")),
    path("studies/", include("apps.studies.urls")),
    path('ratings/', include("apps.ratings.urls")),
    path('rage/', include("apps.rage.urls")),
    path('contacts/', include("apps.contacts.urls")),
    path('abouts/', include("apps.abouts.urls")), 
    path('services/', include("apps.services.urls")),
    path('news/', include("apps.news.urls")),  
]


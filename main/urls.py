
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

api_urlpatterns = [
    path('', include('apps.users.urls')),
    path('', include('apps.abouts.urls')),
    path('', include('apps.tracks.urls')),
    path('', include('apps.ratings.urls')),
    path('', include('apps.studies.urls')),
    path('', include('apps.rage.urls')),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('', include('apps.contacts.urls')),
    path('', include('apps.services.urls')),
    path('', include('apps.news.urls')),
    path('', include('apps.services.urls')),
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

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
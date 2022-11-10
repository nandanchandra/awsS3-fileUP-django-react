from django.conf import settings  
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="AWS S3 IMAGE API",
        default_version="v1",
        description="API Endpoints For Uploading Image into S3",
        contact=openapi.Contact(email="chandranandan16@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('',schema_view.with_ui(cache_timeout=0)),
    path('admin/', admin.site.urls),
    path('api/image/', include('api.image_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
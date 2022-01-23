from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import*
from django.conf import settings


urlpatterns = [
    path('gab-admin/', admin.site.urls),

    path('', include('services.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

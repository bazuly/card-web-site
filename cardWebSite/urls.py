from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('portfolio/', include('website.urls'), name='website'),

              ] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)

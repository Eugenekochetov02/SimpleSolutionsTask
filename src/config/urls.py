"""
URL configuration for config project.

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from apps.items.views import item, items

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', items, name="items"),  # List items
    path('item/', item, name="item"),  # Item

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

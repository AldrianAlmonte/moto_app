from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('posts/', include('posts.urls')),
]

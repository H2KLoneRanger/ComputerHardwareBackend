from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from ComputerHardwareBackEnd import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('cpus.urls')),
    path('', include('mainboards.urls')),
    path('', include('gpus.urls')),
    path('', include('memories.urls')),
    path('', include('ssds.urls')),
    path('', include('hdds.urls')),
    path('', include('powers.urls')),
    path('', include('cases.urls')),

    re_path(r'^static(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]

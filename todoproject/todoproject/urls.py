from django.conf import settings
from django.contrib import admin

from django.urls import include,path


from django.urls import include, re_path
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('todoapp.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

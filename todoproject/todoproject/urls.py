from django.conf import settings
from django.contrib import admin
from django.urls import include,path

from django.views.static import serve
from django.conf.urls import url 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('todoapp.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
]

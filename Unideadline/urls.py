from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # forward root to todolist
    url(r'^', include('todolist.urls', namespace="todolist")),
    url(r'^todolist/', include('todolist.urls', namespace="todolist")),
    url(r'^admin/', include(admin.site.urls)),
)

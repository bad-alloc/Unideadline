from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # forward root to todolist
    url(r'^', include('todolist.urls', namespace="todolist")),
    url(r'^todolist/', include('todolist.urls', namespace="todolist")),
    url(r'^ressources/$', include('todolist.urls', namespace="todolist")), # TODO: Maybe put it under todolist/ressources instead of toplevel?
    url(r'^admin/', include(admin.site.urls)),
)

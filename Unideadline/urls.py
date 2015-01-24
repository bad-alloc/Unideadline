from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Unideadline.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^todolist/', include('todolist.urls', namespace="todolist")),
    url(r'^admin/', include(admin.site.urls)),
)

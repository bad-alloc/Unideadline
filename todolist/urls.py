from django.conf.urls import patterns, url

from todolist import views

urlpatterns = patterns('',
    url(r'^$', views.TodoListView.as_view(), name='index'),
    url(r'^todolist/$', views.TodoListView.as_view(), name='index'),
    url(r'^add_todo/$', views.add_todo, name='add_todo'),
    url(r'^remove_todo/$', views.remove_todo, name='remove_todo'),
)

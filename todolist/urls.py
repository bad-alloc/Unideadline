from django.conf.urls import patterns, url

from todolist import views

urlpatterns = patterns('',
    url(r'^$', views.TodoListView.as_view(), name='index'),
    url(r'^todolist/$', views.TodoListView.as_view(), name='index'),
    url(r'^ressources/$', views.RessourceView.as_view(), name='ressource'),
    url(r'^add_ressource/$', views.add_ressource, name='add_ressource'),
    url(r'^add_todo/$', views.add_todo, name='add_todo'),
    url(r'^remove_todo/$', views.remove_todo, name='remove_todo'),
)

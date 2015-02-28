from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from todolist.models import *

class TodoListView(generic.ListView):
    template_name = 'todolist/index.html'
    context_object_name = 'todo_data'

    def get_context_data(self, **kwargs):
        context = super(generic.ListView, self).get_context_data(**kwargs)
        context['todo_items'] = TodoItem.objects.all()
        context['todo_types'] = TodoType.objects.all()
        return context

    def get_queryset(self):
        """Return all todo items."""
        return TodoItem.objects.all()

    
#def add_todo(request, new_todo_text):
def add_todo(request):
    html = "<html><body>Got something:</br>POST: " + request.POST.get("new_todo_text", "") + "</body></html>"
    return HttpResponse(html)

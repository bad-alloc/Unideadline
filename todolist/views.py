import datetime

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

def add_todo(request):
    raw_priority = request.POST.get("new_todo_priority", "")

    try:
        new_priority = int(raw_priority)
    except ValueError:
        new_priority = 1
    
    new_todo = TodoItem(priority = new_priority,
                        todo_type = TodoType.objects.get(type_tag_name=request.POST.get("new_todo_tag", "")), #TODO: use ID
                        todo_text = request.POST.get("new_todo_text", ""),
                        todo_description = request.POST.get("new_todo_description", ""),
                        deadline = datetime.datetime.now())
    new_todo.save()

    # Ensure we stay on the todo page.
    return HttpResponseRedirect(reverse('todolist:index'))

def remove_todo(request):
    if not request.POST.get("remove", "") == '':
        TodoItem.objects.filter(id = request.POST.get("remove", "")).delete()
    elif not request.POST.get("set", "") == '':
        pass
    else:
        print "ILLEGAL REMOVE REQUEST:", request.POST

        
    return HttpResponseRedirect(reverse('todolist:index'))

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

class RessourceView(generic.ListView):
    template_name = 'todolist/ressources.html'
    context_object_name = 'ressource_data'

    def get_context_data(self, **kwargs):
        context = super(generic.ListView, self).get_context_data(**kwargs)
        context['ressource_items'] = Ressource.objects.all()
        context['ressource_types'] = RessourceType.objects.all()
        return context

    def get_queryset(self):
        """Return all todo items."""
        return Ressource.objects.all()

def safe_number_parse(string):
    try:
        new_priority = int(string)
    except ValueError:
        new_priority = 1
    return new_priority
    
def add_todo(request):
    # Ensure we have some numeric priority so we can sort the todo list by priority later
    new_priority = safe_number_parse(request.POST.get("new_todo_priority", ""))

    # Create a new item and store it to the database
    new_todo = TodoItem(priority = new_priority,
                        todo_type = TodoType.objects.get(id = request.POST.get("new_todo_tag", "")),
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
        item_to_update = TodoItem.objects.get(id = request.POST.get("set", ""))
        item_to_update.todo_type = TodoType.objects.get(id=request.POST.get("set_todo_tag", ""))
        try:
            new_priority = int(request.POST.get("todo_priority", ""))
            item_to_update.priority = new_priority
        except ValueError:
            pass
        item_to_update.save()
    else:
        print "ILLEGAL REMOVE REQUEST:", request.POST

        
    return HttpResponseRedirect(reverse('todolist:index'))

def add_ressource(request):
    new_maxpts = safe_number_parse(request.POST.get("new_ressource_maxpts", ""))
    new_ressource_name = request.POST.get("new_ressource_name", "")
    new_ressource_tag = request.POST.get("new_ressource_tag", "")
    
    new_ressource = Ressource(ressource_name = new_ressource_name,
                              ressource_type = RessourceType.objects.get(id = request.POST.get("new_ressource_tag", "")),
                              ressource_location = "None",
                              associated_todo_item = None,
                              max_credit = new_maxpts,
                              obtained_credit = 0)

    new_ressource.save()
    
    return HttpResponseRedirect(reverse('todolist:ressource'))


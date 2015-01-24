from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from todolist.models import *

class TodoListView(generic.ListView):
    template_name = 'todolist/index.html'
    context_object_name = 'todo_item_list'

    def get_queryset(self):
        """Return all todo items."""
        return TodoItem.objects.all()

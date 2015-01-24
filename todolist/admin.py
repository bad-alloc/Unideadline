from django.contrib import admin

from todolist.models import *

# Register your models here.
admin.site.register(StudentGroup)
admin.site.register(Student)
admin.site.register(RessourceType)
admin.site.register(Ressource)
admin.site.register(TodoType)
admin.site.register(TodoItem)

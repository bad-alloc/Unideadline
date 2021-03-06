from django.db import models
from django.contrib.auth.models import User

# Students can join groups to work together
class StudentGroup(models.Model):
    group_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.group_name

# Students are users which belong to studnet groups
class Student(User):
    group = models.ForeignKey(StudentGroup)

# A task might be centered on Exercise sheets, presentations
# etc. These are the different types. Types are entered by users.
class RessourceType(models.Model):
    ressource_name = models.CharField(max_length=20)
    ressource_description = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.ressource_name
    
# Ressources belong to todo items, like exercise sheets which have to be done.
class Ressource(models.Model):
    ressource_name = models.CharField(max_length=200, default='None')
    ressource_type = models.ForeignKey(RessourceType)
    
    # This way TodoItems can have many Ressources
    # We allow null and blank fields because ressources initially have no associated todo
    associated_todo_item = models.ForeignKey('TodoItem', null=True, blank=True)

    max_credit = models.IntegerField()
    obtained_credit = models.IntegerField()
 
    def __unicode__(self):
        return self.ressource_name

# URLs to locate ressources, each ressource can have many URLs
class URL(models.Model):
    url_string = models.CharField(max_length=1000, default='')
    ressource = models.ForeignKey(Ressource)
    
    def __unicode__(self):
        return self.url_string
    
# Like emcas org mode, there can be different todo tags, like TODO
# DONE CANCELLED etc.
class TodoType(models.Model):
    # Stuff like TODO(Red) DONE(green) etc.
    type_tag_name = models.CharField(max_length=10)
    type_tag_description = models.CharField(max_length=1000)
    type_color_red = models.IntegerField()
    type_color_green = models.IntegerField()
    type_color_blue = models.IntegerField()

    def __unicode__(self):
        return self.type_tag_name

# TodoItems are tasks that are created by users in order to coordinate
# work on different ressources until some deadline.
class TodoItem(models.Model):
    #owner = models.ForeignKey(Student, related_name = 'item_owner')
    #assignee = models.ForeignKey(Student, related_name = 'item_assignee')
    priority = models.IntegerField()

    todo_type = models.ForeignKey(TodoType)
    todo_text = models.CharField(max_length=200)
    todo_description = models.CharField(max_length=1000)
    deadline = models.DateTimeField()

    # A TodoItem can have multiple Ressources. In order to model this,
    # each ressource belongs to one TodoItem, i.e. it holds a foreign
    # key to a TodoItem.

    # Furthermore, Tasks are shared in a group. Everyone in that group
    # can see tasks.
    #group = models.ForeignKey(StudentGroup)

    def __unicode__(self):
        return self.todo_type.type_tag_name + ":" + self.todo_text + " -> " + self.todo_description

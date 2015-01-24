# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ressource_location', models.URLField(max_length=500)),
                ('max_credit', models.IntegerField()),
                ('obtained_credit', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RessourceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ressource_name', models.CharField(max_length=20)),
                ('ressource_description', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.IntegerField()),
                ('todo_text', models.CharField(max_length=200)),
                ('todo_description', models.CharField(max_length=1000)),
                ('deadline', models.DateTimeField()),
                ('assignee', models.ForeignKey(related_name='item_assignee', to='todolist.Student')),
                ('group', models.ForeignKey(to='todolist.StudentGroup')),
                ('owner', models.ForeignKey(related_name='item_owner', to='todolist.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TodoType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_tag_name', models.CharField(max_length=10)),
                ('type_tag_description', models.CharField(max_length=1000)),
                ('type_color_red', models.IntegerField()),
                ('type_color_green', models.IntegerField()),
                ('type_color_blue', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='todo_type',
            field=models.ForeignKey(to='todolist.TodoType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(to='todolist.StudentGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ressource',
            name='associated_todo_item',
            field=models.ForeignKey(to='todolist.TodoItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ressource',
            name='ressource_type',
            field=models.ForeignKey(to='todolist.RessourceType'),
            preserve_default=True,
        ),
    ]

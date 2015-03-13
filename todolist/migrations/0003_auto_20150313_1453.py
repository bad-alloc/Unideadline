# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20150228_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='ressource',
            name='ressource_name',
            field=models.CharField(default=b'None', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ressource',
            name='associated_todo_item',
            field=models.ForeignKey(blank=True, to='todolist.TodoItem', null=True),
            preserve_default=True,
        ),
    ]

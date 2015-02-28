# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='group',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='owner',
        ),
    ]

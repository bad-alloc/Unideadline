# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ressource',
            name='ressource_location',
        ),
    ]

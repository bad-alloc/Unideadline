# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20150313_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_string', models.CharField(default=b'', max_length=1000)),
                ('ressource', models.ForeignKey(to='todolist.Ressource')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

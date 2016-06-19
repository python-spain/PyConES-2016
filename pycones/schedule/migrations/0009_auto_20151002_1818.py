# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_auto_20150930_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slot',
            options={'ordering': ['day', 'start', 'end', 'default_room__order']},
        ),
        migrations.AddField(
            model_name='slot',
            name='default_room',
            field=models.ForeignKey(to='schedule.Room', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='slot',
            field=models.OneToOneField(to='schedule.Slot', related_name='content_ptr', blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='name_ca',
        ),
        migrations.RemoveField(
            model_name='section',
            name='name_eu',
        ),
        migrations.RemoveField(
            model_name='section',
            name='name_ga',
        ),
        migrations.RemoveField(
            model_name='section',
            name='slug_ca',
        ),
        migrations.RemoveField(
            model_name='section',
            name='slug_eu',
        ),
        migrations.RemoveField(
            model_name='section',
            name='slug_ga',
        ),
    ]

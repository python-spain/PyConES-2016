# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsorship', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsorlevel',
            name='description_ca',
        ),
        migrations.RemoveField(
            model_name='sponsorlevel',
            name='description_eu',
        ),
        migrations.RemoveField(
            model_name='sponsorlevel',
            name='description_ga',
        ),
        migrations.RemoveField(
            model_name='sponsorlevel',
            name='name_ca',
        ),
        migrations.RemoveField(
            model_name='sponsorlevel',
            name='name_eu',
        ),
        migrations.RemoveField(
            model_name='sponsorlevel',
            name='name_ga',
        ),
    ]

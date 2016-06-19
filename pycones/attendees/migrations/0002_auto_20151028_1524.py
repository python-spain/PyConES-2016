# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='barcode',
            field=models.CharField(blank=True, null=True, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='dni',
            field=models.CharField(blank=True, null=True, max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='tracker',
            field=models.CharField(blank=True, null=True, max_length=16, verbose_name='localizador ticketea', unique=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendees', '0002_auto_20151028_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='restore_code',
            field=models.CharField(null=True, max_length=16, unique=True, blank=True),
        ),
    ]

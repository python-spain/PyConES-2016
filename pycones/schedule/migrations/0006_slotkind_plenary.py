# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20150918_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='slotkind',
            name='plenary',
            field=models.BooleanField(default=False),
        ),
    ]

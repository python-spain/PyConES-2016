# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0002_auto_20150626_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='name_ca',
            field=models.CharField(verbose_name='name', null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='section',
            name='slug_ca',
            field=models.SlugField(null=True),
        ),
    ]

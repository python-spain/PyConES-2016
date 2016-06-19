# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0003_auto_20150918_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='name_eu',
            field=models.CharField(null=True, max_length=100, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='section',
            name='name_gl',
            field=models.CharField(null=True, max_length=100, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='section',
            name='slug_eu',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='slug_gl',
            field=models.SlugField(null=True),
        ),
    ]

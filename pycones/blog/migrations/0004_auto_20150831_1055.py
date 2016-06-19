# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150626_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug_en',
            field=models.SlugField(blank=True, max_length=128, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug_es',
            field=models.SlugField(blank=True, max_length=128, unique=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_auto_20150626_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='biography_en_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='biography_es_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='biography_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', blank=True),
        ),
    ]

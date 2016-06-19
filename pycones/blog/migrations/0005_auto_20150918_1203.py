# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150831_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='_content_ca_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='content_ca',
            field=markupfield.fields.MarkupField(default='', rendered_field=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ca_markup_type',
            field=models.CharField(default='markdown', max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug_ca',
            field=models.SlugField(max_length=128, unique=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ca',
            field=models.TextField(null=True),
        ),
    ]

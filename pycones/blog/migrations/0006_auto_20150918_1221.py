# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150918_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='_content_eu_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='_content_gl_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='content_eu',
            field=markupfield.fields.MarkupField(null=True, default='', rendered_field=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_eu_markup_type',
            field=models.CharField(default='markdown', max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_gl',
            field=markupfield.fields.MarkupField(null=True, default='', rendered_field=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_gl_markup_type',
            field=models.CharField(default='markdown', max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug_eu',
            field=models.SlugField(null=True, max_length=128, unique=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug_gl',
            field=models.SlugField(null=True, max_length=128, unique=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_eu',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_gl',
            field=models.TextField(null=True),
        ),
    ]

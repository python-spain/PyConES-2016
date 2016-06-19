# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='_content_ca_rendered',
            field=models.TextField(editable=False, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='_content_eu_rendered',
            field=models.TextField(editable=False, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='_content_ga_rendered',
            field=models.TextField(editable=False, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='content_ca',
            field=markupfield.fields.MarkupField(rendered_field=True, default='', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ca_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_eu',
            field=markupfield.fields.MarkupField(rendered_field=True, default='', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_eu_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ga',
            field=markupfield.fields.MarkupField(rendered_field=True, default='', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ga_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug_ca',
            field=models.SlugField(unique=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug_eu',
            field=models.SlugField(unique=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug_ga',
            field=models.SlugField(unique=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ca',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_eu',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ga',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_en_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_es_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='_content_override_ca_rendered',
            field=models.TextField(editable=False, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slot',
            name='_content_override_en_rendered',
            field=models.TextField(editable=False, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slot',
            name='_content_override_es_rendered',
            field=models.TextField(editable=False, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slot',
            name='_content_override_eu_rendered',
            field=models.TextField(editable=False, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slot',
            name='_content_override_ga_rendered',
            field=models.TextField(editable=False, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_ca',
            field=markupfield.fields.MarkupField(blank=True, null=True, rendered_field=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_ca_markup_type',
            field=models.CharField(blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None),
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_en',
            field=markupfield.fields.MarkupField(blank=True, null=True, rendered_field=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_en_markup_type',
            field=models.CharField(blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None),
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_es',
            field=markupfield.fields.MarkupField(blank=True, null=True, rendered_field=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_es_markup_type',
            field=models.CharField(blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None),
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_eu',
            field=markupfield.fields.MarkupField(blank=True, null=True, rendered_field=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_eu_markup_type',
            field=models.CharField(blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None),
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_ga',
            field=markupfield.fields.MarkupField(blank=True, null=True, rendered_field=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_ga_markup_type',
            field=models.CharField(blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None),
        ),
    ]

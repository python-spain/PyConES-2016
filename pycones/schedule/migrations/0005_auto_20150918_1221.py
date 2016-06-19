# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20150918_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='_abstract_eu_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presentation',
            name='_abstract_gl_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presentation',
            name='_description_eu_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presentation',
            name='_description_gl_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presentation',
            name='abstract_eu',
            field=markupfield.fields.MarkupField(null=True, rendered_field=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='abstract_eu_markup_type',
            field=models.CharField(default=None, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='abstract_gl',
            field=markupfield.fields.MarkupField(null=True, rendered_field=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='abstract_gl_markup_type',
            field=models.CharField(default=None, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='description_eu',
            field=markupfield.fields.MarkupField(null=True, rendered_field=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='description_eu_markup_type',
            field=models.CharField(default=None, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='description_gl',
            field=markupfield.fields.MarkupField(null=True, rendered_field=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='description_gl_markup_type',
            field=models.CharField(default=None, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='title_eu',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='presentation',
            name='title_gl',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='room',
            name='name_eu',
            field=models.CharField(null=True, max_length=65),
        ),
        migrations.AddField(
            model_name='room',
            name='name_gl',
            field=models.CharField(null=True, max_length=65),
        ),
        migrations.AddField(
            model_name='slot',
            name='_content_override_eu_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slot',
            name='_content_override_gl_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_eu',
            field=markupfield.fields.MarkupField(null=True, rendered_field=True, blank=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_eu_markup_type',
            field=models.CharField(default=None, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_gl',
            field=markupfield.fields.MarkupField(null=True, rendered_field=True, blank=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_gl_markup_type',
            field=models.CharField(default=None, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='slotkind',
            name='label_eu',
            field=models.CharField(null=True, max_length=50),
        ),
        migrations.AddField(
            model_name='slotkind',
            name='label_gl',
            field=models.CharField(null=True, max_length=50),
        ),
    ]

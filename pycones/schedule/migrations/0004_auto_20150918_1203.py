# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20150626_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='_abstract_ca_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presentation',
            name='_description_ca_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presentation',
            name='abstract_ca',
            field=markupfield.fields.MarkupField(rendered_field=True, null=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='abstract_ca_markup_type',
            field=models.CharField(default=None, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='description_ca',
            field=markupfield.fields.MarkupField(rendered_field=True, null=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='description_ca_markup_type',
            field=models.CharField(default=None, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='title_ca',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='room',
            name='name_ca',
            field=models.CharField(null=True, max_length=65),
        ),
        migrations.AddField(
            model_name='slot',
            name='_content_override_ca_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_ca',
            field=markupfield.fields.MarkupField(rendered_field=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='content_override_ca_markup_type',
            field=models.CharField(default=None, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='slotkind',
            name='label_ca',
            field=models.CharField(null=True, max_length=50),
        ),
    ]

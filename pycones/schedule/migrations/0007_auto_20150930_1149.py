# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_slotkind_plenary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='abstract',
            field=markupfield.fields.MarkupField(rendered_field=True, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='abstract_ca',
            field=markupfield.fields.MarkupField(null=True, default='', blank=True, rendered_field=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='abstract_en',
            field=markupfield.fields.MarkupField(null=True, default='', blank=True, rendered_field=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='abstract_es',
            field=markupfield.fields.MarkupField(null=True, default='', blank=True, rendered_field=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='abstract_eu',
            field=markupfield.fields.MarkupField(null=True, default='', blank=True, rendered_field=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='abstract_gl',
            field=markupfield.fields.MarkupField(null=True, default='', blank=True, rendered_field=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='abstract_markup_type',
            field=models.CharField(blank=True, default=None, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], max_length=30),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='description',
            field=markupfield.fields.MarkupField(rendered_field=True, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='description_ca',
            field=markupfield.fields.MarkupField(null=True, default='', blank=True, rendered_field=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='description_en',
            field=markupfield.fields.MarkupField(null=True, default='', blank=True, rendered_field=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='description_es',
            field=markupfield.fields.MarkupField(null=True, default='', blank=True, rendered_field=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='description_eu',
            field=markupfield.fields.MarkupField(null=True, default='', blank=True, rendered_field=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='description_gl',
            field=markupfield.fields.MarkupField(null=True, default='', blank=True, rendered_field=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='description_markup_type',
            field=models.CharField(blank=True, default=None, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], max_length=30),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='title',
            field=models.CharField(default='', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='title_ca',
            field=models.CharField(null=True, default='', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='title_en',
            field=models.CharField(null=True, default='', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='title_es',
            field=models.CharField(null=True, default='', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='title_eu',
            field=models.CharField(null=True, default='', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='title_gl',
            field=models.CharField(null=True, default='', blank=True, max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_auto_20150930_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='abstract_ca_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='abstract_en_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='abstract_es_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='abstract_eu_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='abstract_gl_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='abstract_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='description_ca_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='description_en_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='description_es_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='description_eu_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='description_gl_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='description_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='slot',
            name='content_override_ca_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='slot',
            name='content_override_en_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='slot',
            name='content_override_es_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='slot',
            name='content_override_eu_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='slot',
            name='content_override_gl_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
        migrations.AlterField(
            model_name='slot',
            name='content_override_markup_type',
            field=models.CharField(default='markdown', blank=True, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')]),
        ),
    ]

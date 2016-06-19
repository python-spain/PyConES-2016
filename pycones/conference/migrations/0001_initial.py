# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=100)),
                ('name_es', models.CharField(null=True, verbose_name='name', max_length=100)),
                ('name_ca', models.CharField(null=True, verbose_name='name', max_length=100)),
                ('name_eu', models.CharField(null=True, verbose_name='name', max_length=100)),
                ('name_ga', models.CharField(null=True, verbose_name='name', max_length=100)),
                ('name_en', models.CharField(null=True, verbose_name='name', max_length=100)),
                ('slug', models.SlugField()),
                ('slug_es', models.SlugField(null=True)),
                ('slug_ca', models.SlugField(null=True)),
                ('slug_eu', models.SlugField(null=True)),
                ('slug_ga', models.SlugField(null=True)),
                ('slug_en', models.SlugField(null=True)),
                ('start_date', models.DateField(null=True, blank=True, verbose_name='start date')),
                ('end_date', models.DateField(null=True, blank=True, verbose_name='end date')),
            ],
            options={
                'verbose_name': 'section',
                'ordering': ['start_date'],
                'verbose_name_plural': 'sections',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-05 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0013_auto_20160723_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=120)),
                ('name_es', models.TextField(max_length=120, null=True)),
                ('name_ca', models.TextField(max_length=120, null=True)),
                ('name_gl', models.TextField(max_length=120, null=True)),
                ('name_eu', models.TextField(max_length=120, null=True)),
                ('name_en', models.TextField(max_length=120, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_workshop', models.BooleanField(default=False)),
            ],
        ),
    ]

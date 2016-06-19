# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150505_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='_content_ca_rendered',
        ),
        migrations.RemoveField(
            model_name='post',
            name='_content_eu_rendered',
        ),
        migrations.RemoveField(
            model_name='post',
            name='_content_ga_rendered',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_ca',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_ca_markup_type',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_eu',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_eu_markup_type',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_ga',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_ga_markup_type',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug_ca',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug_eu',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug_ga',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_ca',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_eu',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_ga',
        ),
    ]

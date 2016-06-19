# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_auto_20151002_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='keynote',
            field=models.FileField(null=True, verbose_name='keynote file', upload_to='keynotes', blank=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='keynote_url',
            field=models.URLField(null=True, verbose_name='keynote URL', blank=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='video_url',
            field=models.URLField(null=True, verbose_name='video URL', blank=True),
        ),
    ]

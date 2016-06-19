# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0011_auto_20160129_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='keynote',
            field=models.FileField(null=True, blank=True, upload_to='keynotes', verbose_name='keynote file'),
        ),
        migrations.AddField(
            model_name='slot',
            name='keynote_url',
            field=models.URLField(null=True, blank=True, verbose_name='keynote URL'),
        ),
        migrations.AddField(
            model_name='slot',
            name='video_url',
            field=models.URLField(null=True, blank=True, verbose_name='video URL'),
        ),
    ]

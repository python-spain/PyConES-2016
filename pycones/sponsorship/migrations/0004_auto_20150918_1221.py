# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsorship', '0003_auto_20150918_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorlevel',
            name='description_eu',
            field=models.TextField(null=True, help_text='This is private.', blank=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='sponsorlevel',
            name='description_gl',
            field=models.TextField(null=True, help_text='This is private.', blank=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='sponsorlevel',
            name='name_eu',
            field=models.CharField(null=True, max_length=100, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='sponsorlevel',
            name='name_gl',
            field=models.CharField(null=True, max_length=100, verbose_name='name'),
        ),
    ]

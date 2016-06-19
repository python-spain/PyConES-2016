# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsorship', '0002_auto_20150626_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorlevel',
            name='description_ca',
            field=models.TextField(verbose_name='description', help_text='This is private.', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sponsorlevel',
            name='name_ca',
            field=models.CharField(verbose_name='name', null=True, max_length=100),
        ),
    ]

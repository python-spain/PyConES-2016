# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='_biography_ca_rendered',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='_biography_eu_rendered',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='_biography_ga_rendered',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='biography_ca',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='biography_ca_markup_type',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='biography_eu',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='biography_eu_markup_type',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='biography_ga',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='biography_ga_markup_type',
        ),
    ]

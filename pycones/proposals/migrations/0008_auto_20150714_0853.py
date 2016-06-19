# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0007_auto_20150714_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='audience_level',
            field=models.CharField(max_length=32, default='basic', choices=[('basic', 'Básico'), ('intermediate', 'Intermedio'), ('advanced', 'Avanzado')], verbose_name='Nivel de la audiencia', null=True),
        ),
    ]

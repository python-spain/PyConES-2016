# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0006_auto_20150713_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='audience_level',
            field=models.CharField(null=True, default='basic', choices=[('basic', 'Básico'), ('intermediate', 'Intermedio'), ('advanced', 'Avanzado')], max_length=32),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='kind',
            field=models.ForeignKey(to='proposals.ProposalKind', verbose_name='Tipo de propuesta'),
        ),
    ]

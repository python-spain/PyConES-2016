# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendees', '0004_auto_20151101_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='allergies',
            field=models.TextField(blank=True, null=True, help_text='Alergias, dieta especial o cualquier cosas que quieres que tengamos en cuenta para el catering. Se hará lo posible por ajustarse a las necesidades particulares.', verbose_name='Consideraciones para el catering'),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='dni',
            field=models.CharField(blank=True, unique=True, null=True, default=None, verbose_name='DNI', max_length=16),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='name',
            field=models.CharField(blank=True, null=True, verbose_name='Nombre completo y apellidos', max_length=128),
        ),
    ]

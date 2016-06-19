# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendees', '0003_attendee_restore_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='workshop_attendance',
            field=models.NullBooleanField(verbose_name='¿Vas a asistir a los talleres del viernes?'),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='allergies',
            field=models.TextField(null=True, blank=True, verbose_name='Alergias'),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='dni',
            field=models.CharField(null=True, unique=True, blank=True, verbose_name='DNI', max_length=16),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='email',
            field=models.EmailField(null=True, blank=True, verbose_name='Email', max_length=128),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='name',
            field=models.CharField(null=True, blank=True, verbose_name='Nombre', max_length=128),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='notes',
            field=models.TextField(null=True, blank=True, verbose_name='Notas'),
        ),
    ]

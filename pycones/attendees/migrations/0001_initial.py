# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', editable=False, default=django.utils.timezone.now, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', editable=False, default=django.utils.timezone.now, blank=True)),
                ('name', models.CharField(null=True, max_length=128, blank=True)),
                ('email', models.EmailField(null=True, max_length=128, blank=True)),
                ('dni', models.CharField(unique=True, max_length=16)),
                ('barcode', models.CharField(unique=True, max_length=32)),
                ('tracker', models.CharField(unique=True, max_length=16, verbose_name='localizador ticketea')),
                ('notes', models.TextField(null=True, blank=True)),
                ('allergies', models.TextField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
    ]

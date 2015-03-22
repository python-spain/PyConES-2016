# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields
import core.helpers.files
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(blank=True, editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(blank=True, editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('status', models.PositiveIntegerField(default=0, choices=[(0, 'Draft'), (1, 'Scheduled'), (2, 'Published')])),
                ('title', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('outstanding_image', models.ImageField(blank=True, null=True, upload_to=core.helpers.files.UploadToDir('images', random_name=False))),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.Tag'),
            preserve_default=True,
        ),
    ]

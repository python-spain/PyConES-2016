# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields
import django.utils.timezone
import core.helpers.files
import django_extensions.db.fields
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
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', editable=False, blank=True, default=django.utils.timezone.now)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', editable=False, blank=True, default=django.utils.timezone.now)),
                ('status', models.PositiveIntegerField(default=0, choices=[(0, 'Draft'), (1, 'Scheduled'), (2, 'Published')])),
                ('title', models.TextField()),
                ('title_en', models.TextField(null=True)),
                ('title_es', models.TextField(null=True)),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('slug_en', models.SlugField(unique=True, blank=True, null=True)),
                ('slug_es', models.SlugField(unique=True, blank=True, null=True)),
                ('content', markupfield.fields.MarkupField(rendered_field=True, blank=True, default='')),
                ('content_en', markupfield.fields.MarkupField(rendered_field=True, blank=True, default='', null=True)),
                ('content_es', markupfield.fields.MarkupField(rendered_field=True, blank=True, default='', null=True)),
                ('content_markup_type', models.CharField(blank=True, default=None, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')])),
                ('scheduled_at', models.DateTimeField(blank=True, null=True)),
                ('content_en_markup_type', models.CharField(blank=True, default=None, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')])),
                ('content_es_markup_type', models.CharField(blank=True, default=None, max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')])),
                ('_content_rendered', models.TextField(editable=False)),
                ('outstanding_image', models.ImageField(blank=True, null=True, upload_to=core.helpers.files.UploadToDir('images', random_name=False))),
                ('_content_en_rendered', models.TextField(editable=False)),
                ('_content_es_rendered', models.TextField(editable=False)),
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
                ('slug', models.SlugField(unique=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', blank=True, to='blog.Tag'),
            preserve_default=True,
        ),
    ]

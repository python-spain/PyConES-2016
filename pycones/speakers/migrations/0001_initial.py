# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(help_text='As you would like it to appear in the conference program.', max_length=100)),
                ('biography', markupfield.fields.MarkupField(help_text="A little bit about you.  Edit using <a href='http://warpedvisions.org/projects/markdown-cheat-sheet/target='_blank'>Markdown</a>.", blank=True, rendered_field=True)),
                ('biography_es', markupfield.fields.MarkupField(null=True, help_text="A little bit about you.  Edit using <a href='http://warpedvisions.org/projects/markdown-cheat-sheet/target='_blank'>Markdown</a>.", blank=True, rendered_field=True)),
                ('biography_ca', markupfield.fields.MarkupField(null=True, help_text="A little bit about you.  Edit using <a href='http://warpedvisions.org/projects/markdown-cheat-sheet/target='_blank'>Markdown</a>.", blank=True, rendered_field=True)),
                ('biography_eu', markupfield.fields.MarkupField(null=True, help_text="A little bit about you.  Edit using <a href='http://warpedvisions.org/projects/markdown-cheat-sheet/target='_blank'>Markdown</a>.", blank=True, rendered_field=True)),
                ('biography_ga', markupfield.fields.MarkupField(null=True, help_text="A little bit about you.  Edit using <a href='http://warpedvisions.org/projects/markdown-cheat-sheet/target='_blank'>Markdown</a>.", blank=True, rendered_field=True)),
                ('biography_en', markupfield.fields.MarkupField(null=True, help_text="A little bit about you.  Edit using <a href='http://warpedvisions.org/projects/markdown-cheat-sheet/target='_blank'>Markdown</a>.", blank=True, rendered_field=True)),
                ('biography_markup_type', models.CharField(blank=True, max_length=30, default=None, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')])),
                ('photo', models.ImageField(blank=True, upload_to='speaker_photos')),
                ('biography_es_markup_type', models.CharField(blank=True, max_length=30, default=None, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')])),
                ('biography_ca_markup_type', models.CharField(blank=True, max_length=30, default=None, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')])),
                ('biography_eu_markup_type', models.CharField(blank=True, max_length=30, default=None, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')])),
                ('biography_ga_markup_type', models.CharField(blank=True, max_length=30, default=None, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')])),
                ('biography_en_markup_type', models.CharField(blank=True, max_length=30, default=None, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')])),
                ('_biography_rendered', models.TextField(editable=False)),
                ('annotation', models.TextField()),
                ('_biography_es_rendered', models.TextField(editable=False)),
                ('_biography_ca_rendered', models.TextField(editable=False)),
                ('_biography_eu_rendered', models.TextField(editable=False)),
                ('_biography_ga_rendered', models.TextField(editable=False)),
                ('_biography_en_rendered', models.TextField(editable=False)),
                ('invite_email', models.CharField(unique=True, null=True, max_length=200, db_index=True)),
                ('invite_token', models.CharField(max_length=40, db_index=True)),
                ('created', models.DateTimeField(editable=False, default=datetime.datetime.now)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, related_name='speaker_profile')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]

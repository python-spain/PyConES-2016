# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0004_auto_20150918_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='_biography_eu_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='_biography_gl_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='biography_eu',
            field=markupfield.fields.MarkupField(null=True, help_text="A little bit about you.  Edit using <a href='http://warpedvisions.org/projects/markdown-cheat-sheet/target='_blank'>Markdown</a>.", rendered_field=True, blank=True),
        ),
        migrations.AddField(
            model_name='speaker',
            name='biography_eu_markup_type',
            field=models.CharField(default='markdown', max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='speaker',
            name='biography_gl',
            field=markupfield.fields.MarkupField(null=True, help_text="A little bit about you.  Edit using <a href='http://warpedvisions.org/projects/markdown-cheat-sheet/target='_blank'>Markdown</a>.", rendered_field=True, blank=True),
        ),
        migrations.AddField(
            model_name='speaker',
            name='biography_gl_markup_type',
            field=models.CharField(default='markdown', max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
    ]

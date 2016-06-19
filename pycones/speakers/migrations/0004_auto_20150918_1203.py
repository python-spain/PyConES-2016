# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0003_auto_20150713_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='_biography_ca_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='biography_ca',
            field=markupfield.fields.MarkupField(rendered_field=True, help_text="A little bit about you.  Edit using <a href='http://warpedvisions.org/projects/markdown-cheat-sheet/target='_blank'>Markdown</a>.", null=True, blank=True),
        ),
        migrations.AddField(
            model_name='speaker',
            name='biography_ca_markup_type',
            field=models.CharField(default='markdown', max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
    ]

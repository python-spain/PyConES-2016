# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0009_auto_20150910_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='description_ca',
            field=models.TextField(verbose_name='Breve descripción', help_text='If your proposal is accepted this will be made public and printed in the program. Should be one paragraph, maximum 500 characters.', null=True, max_length=500),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='_abstract_ca_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='_additional_notes_ca_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='abstract_ca',
            field=markupfield.fields.MarkupField(default='', verbose_name='Resumen detallado', rendered_field=True, null=True, help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>."),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='abstract_ca_markup_type',
            field=models.CharField(default='markdown', max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='additional_notes_ca',
            field=markupfield.fields.MarkupField(rendered_field=True, null=True, blank=True, default='', verbose_name='Notas adicionales', help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. If it's a workshop, specify the duration. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>."),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='additional_notes_ca_markup_type',
            field=models.CharField(default='markdown', max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='title_ca',
            field=models.CharField(verbose_name='Título', null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='proposalkind',
            name='name_ca',
            field=models.CharField(verbose_name='Name', null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='proposalkind',
            name='slug_ca',
            field=models.SlugField(null=True),
        ),
    ]

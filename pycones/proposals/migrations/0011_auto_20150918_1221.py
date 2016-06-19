# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0010_auto_20150918_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='description_eu',
            field=models.TextField(null=True, max_length=500, help_text='If your proposal is accepted this will be made public and printed in the program. Should be one paragraph, maximum 500 characters.', verbose_name='Breve descripción'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='description_gl',
            field=models.TextField(null=True, max_length=500, help_text='If your proposal is accepted this will be made public and printed in the program. Should be one paragraph, maximum 500 characters.', verbose_name='Breve descripción'),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='_abstract_eu_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='_abstract_gl_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='_additional_notes_eu_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='_additional_notes_gl_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='abstract_eu',
            field=markupfield.fields.MarkupField(null=True, help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", default='', rendered_field=True, verbose_name='Resumen detallado'),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='abstract_eu_markup_type',
            field=models.CharField(default='markdown', max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='abstract_gl',
            field=markupfield.fields.MarkupField(null=True, help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", default='', rendered_field=True, verbose_name='Resumen detallado'),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='abstract_gl_markup_type',
            field=models.CharField(default='markdown', max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='additional_notes_eu',
            field=markupfield.fields.MarkupField(help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. If it's a workshop, specify the duration. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", default='', blank=True, null=True, rendered_field=True, verbose_name='Notas adicionales'),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='additional_notes_eu_markup_type',
            field=models.CharField(default='markdown', max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='additional_notes_gl',
            field=markupfield.fields.MarkupField(help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. If it's a workshop, specify the duration. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", default='', blank=True, null=True, rendered_field=True, verbose_name='Notas adicionales'),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='additional_notes_gl_markup_type',
            field=models.CharField(default='markdown', max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], blank=True),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='title_eu',
            field=models.CharField(null=True, max_length=100, verbose_name='Título'),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='title_gl',
            field=models.CharField(null=True, max_length=100, verbose_name='Título'),
        ),
        migrations.AddField(
            model_name='proposalkind',
            name='name_eu',
            field=models.CharField(null=True, max_length=100, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='proposalkind',
            name='name_gl',
            field=models.CharField(null=True, max_length=100, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='proposalkind',
            name='slug_eu',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='proposalkind',
            name='slug_gl',
            field=models.SlugField(null=True),
        ),
    ]

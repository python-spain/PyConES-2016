# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0004_auto_20150713_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='description_en',
            field=models.TextField(max_length=500, help_text='If your proposal is accepted this will be made public and printed in the program. Should be one paragraph, maximum 400 characters.', verbose_name='Breve Descripción', null=True),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='description_es',
            field=models.TextField(max_length=500, help_text='If your proposal is accepted this will be made public and printed in the program. Should be one paragraph, maximum 400 characters.', verbose_name='Breve Descripción', null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract',
            field=markupfield.fields.MarkupField(help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", rendered_field=True, verbose_name='Resumen detallado'),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_en',
            field=markupfield.fields.MarkupField(help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", verbose_name='Resumen detallado', rendered_field=True, null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_en_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', blank=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_es',
            field=markupfield.fields.MarkupField(help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", verbose_name='Resumen detallado', rendered_field=True, null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_es_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', blank=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown'),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes',
            field=markupfield.fields.MarkupField(help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", blank=True, rendered_field=True, verbose_name='Notas adicionales'),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes_en',
            field=markupfield.fields.MarkupField(rendered_field=True, help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", verbose_name='Notas adicionales', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes_en_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', blank=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes_es',
            field=markupfield.fields.MarkupField(rendered_field=True, help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", verbose_name='Notas adicionales', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes_es_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', blank=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', blank=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='description',
            field=models.TextField(max_length=500, help_text='If your proposal is accepted this will be made public and printed in the program. Should be one paragraph, maximum 400 characters.', verbose_name='Breve Descripción'),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='kind',
            field=models.ForeignKey(to='proposals.ProposalKind', verbose_name='Tipo de popuesta'),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='title_en',
            field=models.CharField(max_length=100, verbose_name='Título', null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='title_es',
            field=models.CharField(max_length=100, verbose_name='Título', null=True),
        ),
    ]

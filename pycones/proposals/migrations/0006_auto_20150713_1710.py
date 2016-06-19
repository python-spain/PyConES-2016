# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0005_auto_20150713_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract',
            field=markupfield.fields.MarkupField(verbose_name='Resumen detallado', rendered_field=True, help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", default=''),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_en',
            field=markupfield.fields.MarkupField(null=True, verbose_name='Resumen detallado', rendered_field=True, help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", default=''),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_es',
            field=markupfield.fields.MarkupField(null=True, verbose_name='Resumen detallado', rendered_field=True, help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", default=''),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes',
            field=markupfield.fields.MarkupField(verbose_name='Notas adicionales', blank=True, rendered_field=True, help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", default=''),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes_en',
            field=markupfield.fields.MarkupField(null=True, rendered_field=True, help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", verbose_name='Notas adicionales', default='', blank=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes_es',
            field=markupfield.fields.MarkupField(null=True, rendered_field=True, help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", verbose_name='Notas adicionales', default='', blank=True),
        ),
    ]

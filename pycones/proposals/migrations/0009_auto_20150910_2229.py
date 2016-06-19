# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0008_auto_20150714_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='description_en',
            field=models.TextField(verbose_name='Breve descripción', help_text='If your proposal is accepted this will be made public and printed in the program. Should be one paragraph, maximum 500 characters.', null=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='description_es',
            field=models.TextField(verbose_name='Breve descripción', help_text='If your proposal is accepted this will be made public and printed in the program. Should be one paragraph, maximum 500 characters.', null=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes',
            field=markupfield.fields.MarkupField(verbose_name='Notas adicionales', help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. If it's a workshop, specify the duration. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", rendered_field=True, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes_en',
            field=markupfield.fields.MarkupField(verbose_name='Notas adicionales', help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. If it's a workshop, specify the duration. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", null=True, blank=True, default='', rendered_field=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes_es',
            field=markupfield.fields.MarkupField(verbose_name='Notas adicionales', help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. If it's a workshop, specify the duration. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", null=True, blank=True, default='', rendered_field=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='description',
            field=models.TextField(verbose_name='Breve descripción', help_text='If your proposal is accepted this will be made public and printed in the program. Should be one paragraph, maximum 500 characters.', max_length=500),
        ),
    ]

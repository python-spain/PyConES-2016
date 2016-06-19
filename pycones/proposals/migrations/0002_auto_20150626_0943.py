# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposalbase',
            name='_abstract_ca_rendered',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='_abstract_eu_rendered',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='_abstract_ga_rendered',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='_additional_notes_ca_rendered',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='_additional_notes_eu_rendered',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='_additional_notes_ga_rendered',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='abstract_ca',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='abstract_ca_markup_type',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='abstract_eu',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='abstract_eu_markup_type',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='abstract_ga',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='abstract_ga_markup_type',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='additional_notes_ca',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='additional_notes_ca_markup_type',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='additional_notes_eu',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='additional_notes_eu_markup_type',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='additional_notes_ga',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='additional_notes_ga_markup_type',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='title_ca',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='title_eu',
        ),
        migrations.RemoveField(
            model_name='proposalbase',
            name='title_ga',
        ),
        migrations.RemoveField(
            model_name='proposalkind',
            name='name_ca',
        ),
        migrations.RemoveField(
            model_name='proposalkind',
            name='name_eu',
        ),
        migrations.RemoveField(
            model_name='proposalkind',
            name='name_ga',
        ),
        migrations.RemoveField(
            model_name='proposalkind',
            name='slug_ca',
        ),
        migrations.RemoveField(
            model_name='proposalkind',
            name='slug_eu',
        ),
        migrations.RemoveField(
            model_name='proposalkind',
            name='slug_ga',
        ),
    ]

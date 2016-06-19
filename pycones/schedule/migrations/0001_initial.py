# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0001_initial'),
        ('conference', '0001_initial'),
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField()),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('title_es', models.CharField(null=True, max_length=100)),
                ('title_ca', models.CharField(null=True, max_length=100)),
                ('title_eu', models.CharField(null=True, max_length=100)),
                ('title_ga', models.CharField(null=True, max_length=100)),
                ('title_en', models.CharField(null=True, max_length=100)),
                ('description', markupfield.fields.MarkupField(rendered_field=True)),
                ('description_es', markupfield.fields.MarkupField(null=True, rendered_field=True)),
                ('description_ca', markupfield.fields.MarkupField(null=True, rendered_field=True)),
                ('description_eu', markupfield.fields.MarkupField(null=True, rendered_field=True)),
                ('description_ga', markupfield.fields.MarkupField(null=True, rendered_field=True)),
                ('description_en', markupfield.fields.MarkupField(null=True, rendered_field=True)),
                ('abstract', markupfield.fields.MarkupField(rendered_field=True)),
                ('description_markup_type', models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None)),
                ('abstract_es', markupfield.fields.MarkupField(null=True, rendered_field=True)),
                ('abstract_ca', markupfield.fields.MarkupField(null=True, rendered_field=True)),
                ('abstract_eu', markupfield.fields.MarkupField(null=True, rendered_field=True)),
                ('abstract_ga', markupfield.fields.MarkupField(null=True, rendered_field=True)),
                ('abstract_en', markupfield.fields.MarkupField(null=True, rendered_field=True)),
                ('description_es_markup_type', models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, blank=True)),
                ('description_ca_markup_type', models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, blank=True)),
                ('description_eu_markup_type', models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, blank=True)),
                ('description_ga_markup_type', models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, blank=True)),
                ('description_en_markup_type', models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, blank=True)),
                ('abstract_markup_type', models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None)),
                ('_description_rendered', models.TextField(editable=False)),
                ('abstract_es_markup_type', models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, blank=True)),
                ('abstract_ca_markup_type', models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, blank=True)),
                ('abstract_eu_markup_type', models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, blank=True)),
                ('abstract_ga_markup_type', models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, blank=True)),
                ('abstract_en_markup_type', models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, blank=True)),
                ('_description_es_rendered', models.TextField(editable=False)),
                ('_description_ca_rendered', models.TextField(editable=False)),
                ('_description_eu_rendered', models.TextField(editable=False)),
                ('_description_ga_rendered', models.TextField(editable=False)),
                ('_description_en_rendered', models.TextField(editable=False)),
                ('_abstract_rendered', models.TextField(editable=False)),
                ('_abstract_es_rendered', models.TextField(editable=False)),
                ('_abstract_ca_rendered', models.TextField(editable=False)),
                ('_abstract_eu_rendered', models.TextField(editable=False)),
                ('_abstract_ga_rendered', models.TextField(editable=False)),
                ('_abstract_en_rendered', models.TextField(editable=False)),
                ('cancelled', models.BooleanField(default=False)),
                ('additional_speakers', models.ManyToManyField(related_name='copresentations', to='speakers.Speaker', blank=True)),
                ('proposal_base', models.OneToOneField(to='proposals.ProposalBase', related_name='presentation')),
                ('section', models.ForeignKey(related_name='presentations', to='conference.Section')),
            ],
            options={
                'ordering': ['slot'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=65)),
                ('name_es', models.CharField(null=True, max_length=65)),
                ('name_ca', models.CharField(null=True, max_length=65)),
                ('name_eu', models.CharField(null=True, max_length=65)),
                ('name_ga', models.CharField(null=True, max_length=65)),
                ('name_en', models.CharField(null=True, max_length=65)),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('published', models.BooleanField(default=True)),
                ('hidden', models.BooleanField(verbose_name='Hide schedule from overall conference view', default=False)),
                ('section', models.OneToOneField(to='conference.Section')),
            ],
            options={
                'ordering': ['section'],
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('content_override', markupfield.fields.MarkupField(rendered_field=True, blank=True)),
                ('content_override_markup_type', models.CharField(max_length=30, choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, blank=True)),
                ('_content_override_rendered', models.TextField(editable=False)),
                ('day', models.ForeignKey(to='schedule.Day')),
            ],
            options={
                'ordering': ['day', 'start', 'end'],
            },
        ),
        migrations.CreateModel(
            name='SlotKind',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('label', models.CharField(max_length=50)),
                ('label_es', models.CharField(null=True, max_length=50)),
                ('label_ca', models.CharField(null=True, max_length=50)),
                ('label_eu', models.CharField(null=True, max_length=50)),
                ('label_ga', models.CharField(null=True, max_length=50)),
                ('label_en', models.CharField(null=True, max_length=50)),
                ('schedule', models.ForeignKey(to='schedule.Schedule')),
            ],
        ),
        migrations.CreateModel(
            name='SlotRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('room', models.ForeignKey(to='schedule.Room')),
                ('slot', models.ForeignKey(to='schedule.Slot')),
            ],
            options={
                'ordering': ['slot', 'room__order'],
            },
        ),
        migrations.AddField(
            model_name='slot',
            name='kind',
            field=models.ForeignKey(to='schedule.SlotKind'),
        ),
        migrations.AddField(
            model_name='room',
            name='schedule',
            field=models.ForeignKey(to='schedule.Schedule'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='slot',
            field=models.OneToOneField(related_name='content_ptr', to='schedule.Slot', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='speaker',
            field=models.ForeignKey(related_name='presentations', to='speakers.Speaker'),
        ),
        migrations.AddField(
            model_name='day',
            name='schedule',
            field=models.ForeignKey(to='schedule.Schedule'),
        ),
        migrations.AlterUniqueTogether(
            name='slotroom',
            unique_together=set([('slot', 'room')]),
        ),
        migrations.AlterUniqueTogether(
            name='day',
            unique_together=set([('schedule', 'date')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import proposals.models
from django.conf import settings
import markupfield.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('speakers', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalSpeaker',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Accepted'), (3, 'Declined')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ProposalBase',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_es', models.CharField(null=True, max_length=100)),
                ('title_ca', models.CharField(null=True, max_length=100)),
                ('title_eu', models.CharField(null=True, max_length=100)),
                ('title_ga', models.CharField(null=True, max_length=100)),
                ('title_en', models.CharField(null=True, max_length=100)),
                ('description', models.TextField(verbose_name='Brief Description', help_text='If your proposal is accepted this will be made public and printed in the program. Should be one paragraph, maximum 400 characters.', max_length=400)),
                ('abstract', markupfield.fields.MarkupField(rendered_field=True, verbose_name='Detailed Abstract', help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.")),
                ('abstract_es', markupfield.fields.MarkupField(null=True, verbose_name='Detailed Abstract', rendered_field=True, help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.")),
                ('abstract_ca', markupfield.fields.MarkupField(null=True, verbose_name='Detailed Abstract', rendered_field=True, help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.")),
                ('abstract_eu', markupfield.fields.MarkupField(null=True, verbose_name='Detailed Abstract', rendered_field=True, help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.")),
                ('abstract_ga', markupfield.fields.MarkupField(null=True, verbose_name='Detailed Abstract', rendered_field=True, help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.")),
                ('abstract_en', markupfield.fields.MarkupField(null=True, verbose_name='Detailed Abstract', rendered_field=True, help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.")),
                ('additional_notes', markupfield.fields.MarkupField(rendered_field=True, help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", blank=True)),
                ('abstract_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, max_length=30)),
                ('abstract_es_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, max_length=30, blank=True)),
                ('abstract_ca_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, max_length=30, blank=True)),
                ('abstract_eu_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, max_length=30, blank=True)),
                ('abstract_ga_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, max_length=30, blank=True)),
                ('abstract_en_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, max_length=30, blank=True)),
                ('additional_notes_es', markupfield.fields.MarkupField(null=True, rendered_field=True, help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", blank=True)),
                ('additional_notes_ca', markupfield.fields.MarkupField(null=True, rendered_field=True, help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", blank=True)),
                ('additional_notes_eu', markupfield.fields.MarkupField(null=True, rendered_field=True, help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", blank=True)),
                ('additional_notes_ga', markupfield.fields.MarkupField(null=True, rendered_field=True, help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", blank=True)),
                ('additional_notes_en', markupfield.fields.MarkupField(null=True, rendered_field=True, help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", blank=True)),
                ('submitted', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('additional_notes_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, max_length=30, blank=True)),
                ('_abstract_rendered', models.TextField(editable=False)),
                ('_abstract_es_rendered', models.TextField(editable=False)),
                ('_abstract_ca_rendered', models.TextField(editable=False)),
                ('_abstract_eu_rendered', models.TextField(editable=False)),
                ('_abstract_ga_rendered', models.TextField(editable=False)),
                ('_abstract_en_rendered', models.TextField(editable=False)),
                ('additional_notes_es_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, max_length=30, blank=True)),
                ('additional_notes_ca_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, max_length=30, blank=True)),
                ('additional_notes_eu_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, max_length=30, blank=True)),
                ('additional_notes_ga_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, max_length=30, blank=True)),
                ('additional_notes_en_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default=None, max_length=30, blank=True)),
                ('_additional_notes_rendered', models.TextField(editable=False)),
                ('_additional_notes_es_rendered', models.TextField(editable=False)),
                ('_additional_notes_ca_rendered', models.TextField(editable=False)),
                ('_additional_notes_eu_rendered', models.TextField(editable=False)),
                ('_additional_notes_ga_rendered', models.TextField(editable=False)),
                ('_additional_notes_en_rendered', models.TextField(editable=False)),
                ('cancelled', models.BooleanField(default=False)),
                ('additional_speakers', models.ManyToManyField(through='proposals.AdditionalSpeaker', to='speakers.Speaker', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProposalKind',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
                ('name_es', models.CharField(null=True, verbose_name='Name', max_length=100)),
                ('name_ca', models.CharField(null=True, verbose_name='Name', max_length=100)),
                ('name_eu', models.CharField(null=True, verbose_name='Name', max_length=100)),
                ('name_ga', models.CharField(null=True, verbose_name='Name', max_length=100)),
                ('name_en', models.CharField(null=True, verbose_name='Name', max_length=100)),
                ('slug', models.SlugField()),
                ('slug_es', models.SlugField(null=True)),
                ('slug_ca', models.SlugField(null=True)),
                ('slug_eu', models.SlugField(null=True)),
                ('slug_ga', models.SlugField(null=True)),
                ('slug_en', models.SlugField(null=True)),
                ('section', models.ForeignKey(to='conference.Section', related_name='proposal_kinds')),
            ],
        ),
        migrations.CreateModel(
            name='ProposalSection',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('start', models.DateTimeField(null=True, blank=True)),
                ('end', models.DateTimeField(null=True, blank=True)),
                ('closed', models.NullBooleanField()),
                ('published', models.NullBooleanField()),
                ('section', models.OneToOneField(to='conference.Section')),
            ],
        ),
        migrations.CreateModel(
            name='SupportingDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to=proposals.models.uuid_filename)),
                ('description', models.CharField(max_length=140)),
                ('proposal', models.ForeignKey(to='proposals.ProposalBase', related_name='supporting_documents')),
                ('uploaded_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='kind',
            field=models.ForeignKey(to='proposals.ProposalKind'),
        ),
        migrations.AddField(
            model_name='proposalbase',
            name='speaker',
            field=models.ForeignKey(to='speakers.Speaker', related_name='proposals'),
        ),
        migrations.AddField(
            model_name='additionalspeaker',
            name='proposalbase',
            field=models.ForeignKey(to='proposals.ProposalBase'),
        ),
        migrations.AddField(
            model_name='additionalspeaker',
            name='speaker',
            field=models.ForeignKey(to='speakers.Speaker'),
        ),
        migrations.AlterUniqueTogether(
            name='additionalspeaker',
            unique_together=set([('speaker', 'proposalbase')]),
        ),
    ]

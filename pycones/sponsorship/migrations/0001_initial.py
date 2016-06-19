# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('type', models.CharField(max_length=10, verbose_name='type', default='simple', choices=[('text', 'Text'), ('file', 'File'), ('web_logo', 'Web Logo'), ('simple', 'Simple')])),
            ],
        ),
        migrations.CreateModel(
            name='BenefitLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('max_words', models.PositiveIntegerField(verbose_name='max words', blank=True, null=True)),
                ('other_limits', models.CharField(max_length=200, verbose_name='other limits', blank=True)),
                ('benefit', models.ForeignKey(to='sponsorship.Benefit', verbose_name='benefit', related_name='benefit_levels')),
            ],
            options={
                'ordering': ['level'],
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Sponsor Name')),
                ('external_url', models.URLField(verbose_name='external URL')),
                ('annotation', models.TextField(verbose_name='annotation', blank=True)),
                ('contact_name', models.CharField(max_length=100, verbose_name='Contact Name')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='Contact Email')),
                ('added', models.DateTimeField(verbose_name='added', default=datetime.datetime.now)),
                ('active', models.BooleanField(verbose_name='active', default=False)),
                ('applicant', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='applicant', related_name='sponsorships', null=True)),
            ],
            options={
                'verbose_name': 'sponsor',
                'verbose_name_plural': 'sponsors',
            },
        ),
        migrations.CreateModel(
            name='SponsorBenefit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('max_words', models.PositiveIntegerField(verbose_name='max words', blank=True, null=True)),
                ('other_limits', models.CharField(max_length=200, verbose_name='other limits', blank=True)),
                ('text', models.TextField(verbose_name='text', blank=True)),
                ('upload', models.FileField(verbose_name='file', blank=True, upload_to='sponsor_files')),
                ('benefit', models.ForeignKey(to='sponsorship.Benefit', verbose_name='benefit', related_name='sponsor_benefits')),
                ('sponsor', models.ForeignKey(to='sponsorship.Sponsor', verbose_name='sponsor', related_name='sponsor_benefits')),
            ],
            options={
                'ordering': ['-active'],
            },
        ),
        migrations.CreateModel(
            name='SponsorLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('name_es', models.CharField(max_length=100, verbose_name='name', null=True)),
                ('name_ca', models.CharField(max_length=100, verbose_name='name', null=True)),
                ('name_eu', models.CharField(max_length=100, verbose_name='name', null=True)),
                ('name_ga', models.CharField(max_length=100, verbose_name='name', null=True)),
                ('name_en', models.CharField(max_length=100, verbose_name='name', null=True)),
                ('order', models.IntegerField(verbose_name='order', default=0)),
                ('cost', models.PositiveIntegerField(verbose_name='cost')),
                ('description', models.TextField(verbose_name='description', blank=True, help_text='This is private.')),
                ('description_es', models.TextField(verbose_name='description', blank=True, null=True, help_text='This is private.')),
                ('description_ca', models.TextField(verbose_name='description', blank=True, null=True, help_text='This is private.')),
                ('description_eu', models.TextField(verbose_name='description', blank=True, null=True, help_text='This is private.')),
                ('description_ga', models.TextField(verbose_name='description', blank=True, null=True, help_text='This is private.')),
                ('description_en', models.TextField(verbose_name='description', blank=True, null=True, help_text='This is private.')),
            ],
            options={
                'verbose_name': 'sponsor level',
                'ordering': ['order'],
                'verbose_name_plural': 'sponsor levels',
            },
        ),
        migrations.AddField(
            model_name='sponsor',
            name='level',
            field=models.ForeignKey(verbose_name='level', to='sponsorship.SponsorLevel'),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='sponsor_logo',
            field=models.ForeignKey(to='sponsorship.SponsorBenefit', blank=True, related_name='+', null=True, editable=False),
        ),
        migrations.AddField(
            model_name='benefitlevel',
            name='level',
            field=models.ForeignKey(to='sponsorship.SponsorLevel', verbose_name='level', related_name='benefit_levels'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0003_proposal'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='description_en',
            field=models.TextField(verbose_name='Brief Description', help_text='If your proposal is accepted this will be made public and printed in the program. Should be one paragraph, maximum 400 characters.', null=True, max_length=500),
        ),
        migrations.AddField(
            model_name='proposal',
            name='description_es',
            field=models.TextField(verbose_name='Brief Description', help_text='If your proposal is accepted this will be made public and printed in the program. Should be one paragraph, maximum 400 characters.', null=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='description',
            field=models.TextField(help_text='If your proposal is accepted this will be made public and printed in the program. Should be one paragraph, maximum 400 characters.', verbose_name='Brief Description', max_length=500),
        ),
    ]

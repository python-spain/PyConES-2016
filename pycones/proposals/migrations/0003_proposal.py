# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0002_auto_20150626_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('proposalbase_ptr', models.OneToOneField(to='proposals.ProposalBase', parent_link=True, primary_key=True, auto_created=True, serialize=False)),
                ('paper', models.BooleanField(default=False, help_text='¿Estarías dispuesto a preparar un paper que acompañe la charla?')),
            ],
            bases=('proposals.proposalbase',),
        ),
    ]

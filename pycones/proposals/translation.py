# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import TranslationOptions, translator

from proposals.models import ProposalKind, ProposalBase, Proposal


class ProposalKindTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')


class ProposalBaseTranslationOptions(TranslationOptions):
    fields = ('title', 'abstract', 'additional_notes')


class ProposalTranslationOptions(TranslationOptions):
    fields = ('description', )


translator.register(ProposalKind, ProposalKindTranslationOptions)
translator.register(ProposalBase, ProposalBaseTranslationOptions)
translator.register(Proposal, ProposalTranslationOptions)

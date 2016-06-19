# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import TranslationOptions, translator

from blog.models import Post
from conference.models import Section


class SectionTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')


translator.register(Section, SectionTranslationOptions)

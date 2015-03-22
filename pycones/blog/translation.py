# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import TranslationOptions, translator

from blog.models import Post


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'content')

translator.register(Post, PostTranslationOptions)

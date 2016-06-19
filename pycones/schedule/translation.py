# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import TranslationOptions, translator

from schedule.models import Room, SlotKind, Presentation, Slot


class RoomTranslationOptions(TranslationOptions):
    fields = ('name', )


class SlotKindTranslationOptions(TranslationOptions):
    fields = ('label', )


class PresentationTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'abstract')


class SlotTranslationOptions(TranslationOptions):
    fields = ('content_override', )

translator.register(Room, RoomTranslationOptions)
translator.register(SlotKind, SlotKindTranslationOptions)
translator.register(Presentation, PresentationTranslationOptions)
translator.register(Slot, SlotTranslationOptions)

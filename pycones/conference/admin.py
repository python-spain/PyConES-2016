# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from conference.models import Section

admin.site.register(
    Section,
    prepopulated_fields={"slug": ("name",)},
    list_display=("name", "start_date", "end_date")
)

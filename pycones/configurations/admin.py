# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from configurations.models import Option


@admin.register(Option)
class OptionsAdmin(admin.ModelAdmin):
    """Manage configuration options."""
    list_display = ['public_name', 'value']

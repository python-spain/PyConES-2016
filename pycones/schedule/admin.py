# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from schedule.models import Schedule, Day, Room, SlotKind, Slot, SlotRoom, Presentation


class SlotAdmin(ModelAdmin):
    list_display = ("id", "day", "start", "end", "kind", "default_room", "current_room")

    def current_room(self, instance):
        try:
            return instance.rooms[0]
        except IndexError:
            return None


admin.site.register(Schedule)
admin.site.register(Day)
admin.site.register(Room)
admin.site.register(SlotKind)
admin.site.register(Slot, SlotAdmin)
admin.site.register(
    SlotRoom,
    list_display=("id", "slot", "room")
)
admin.site.register(Presentation)


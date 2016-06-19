# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def update_default_room(apps, schema_editor):
    Slot = apps.get_model("schedule", "Slot")
    Room = apps.get_model("schedule", "Room")
    for slot in Slot.objects.all():
        try:
            room = Room.objects.filter(pk__in=slot.slotroom_set.values("room")).first()
            if room:
                slot.default_room = room
                slot.save()
        except IndexError:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_auto_20151002_1818'),
    ]

    operations = [
        migrations.RunPython(update_default_room),
    ]

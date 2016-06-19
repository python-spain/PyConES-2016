# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from attendees.models import Attendee


class AttendeeAuthBackend(object):
    """Login using tracker and password."""

    def authenticate(self, tracker, password):
        try:
            attendee = Attendee.objects.get(tracker=tracker)
        except Attendee.DoesNotExist:
            return None
        if not attendee.user:
            return None
        user = attendee.user
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

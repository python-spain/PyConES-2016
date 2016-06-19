# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from attendees.views import AttendeeSignInView, RequestRestorePasswordView, RestorePasswordView, EditAttendanceView, \
    LogoutView

urlpatterns = [
    url(r'^sign-in/$', AttendeeSignInView.as_view(), name="sign_in"),
    url(r'^request-restore-password/$', RequestRestorePasswordView.as_view(), name="request_restore_password"),
    url(r'^restore-password/(?P<restore_code>.+)/$', RestorePasswordView.as_view(), name="restore_password"),
    url(r'^profile/$', EditAttendanceView.as_view(), name="profile"),
    url(r'^log-out/$', LogoutView.as_view(), name="log_out"),
]

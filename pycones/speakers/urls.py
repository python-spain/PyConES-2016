# -*- coding: utf-8 -*-
from django.conf.urls import url

from speakers.views import EditSpeaker, SignInView, RequestRestorePasswordView, RestorePasswordView

urlpatterns = [
    url(r'^sign-in/$', SignInView.as_view(), name="sign-in"),
    url(r'^request-restore-password/$', RequestRestorePasswordView.as_view(), name="request_restore_password"),
    url(r'^restore-password/(?P<restore_code>.+)/$', RestorePasswordView.as_view(), name="restore_password"),
    url(r'^$', EditSpeaker.as_view(), name="edit"),
]

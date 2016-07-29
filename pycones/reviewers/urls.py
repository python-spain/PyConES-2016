# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import SignInView, ReviewListView, ReviewView, RequestRestorePasswordView, RestorePasswordView


urlpatterns = [
    url(r'^sign-in/$', SignInView.as_view(), name="sign-in"),
    url(r'^request-restore-password/$', RequestRestorePasswordView.as_view(), name="request_restore_password"),
    url(r'^restore-password/(?P<restore_code>.+)/$', RestorePasswordView.as_view(), name="restore_password"),
    url(r'^(?P<pk>\d+)/$', ReviewView.as_view(), name="details"),
    url(r'^$', ReviewListView.as_view(), name="list"),
]

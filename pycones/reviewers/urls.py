# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from reviewers.views import SignInView, ReviewListView, ReviewView

urlpatterns = [
    url(r'^sign-in/$', SignInView.as_view(), name="sign-in"),
    url(r'^(?P<pk>\d+)/$', ReviewView.as_view(), name="details"),
    url(r'^$', ReviewListView.as_view(), name="list"),
]

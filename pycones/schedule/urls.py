# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from schedule.views import ShowSchedule

urlpatterns = [
    url(r'^$', ShowSchedule.as_view(), name="show"),
]

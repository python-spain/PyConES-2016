# -*- coding: utf-8 -*-
from django.conf.urls import url

from speakers.views import EditSpeaker

urlpatterns = [
    url(r"edit/", EditSpeaker.as_view(), name="edit"),
]

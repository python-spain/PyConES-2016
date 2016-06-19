# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView

from proposals.views import SubmitProposalView

urlpatterns = [
    url(r'^submit/success/$', TemplateView.as_view(template_name='proposals/success.html'), name="success"),
    url(r'^submit/$', SubmitProposalView.as_view(), name="submit"),
]

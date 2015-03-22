# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render
from django.template.base import TemplateDoesNotExist
from django.views.generic import View


class PartialsTemplateView(View):
    """Generic view for load templates from frontend app. Takes an argument form
    url definition, and use it to resolve the requested template.
    """
    external_templates_folder = 'partials/'

    def get(self, request, name):
        """Needs a ``name`` attribute to find the external template.

        :param request:
        :type request: HttpRequest
        :param name:
        :type name: str
        :return: HttpResponse
        """
        template = "{}{}.html".format(self.external_templates_folder, name)
        try:
            return render(request, template)
        except TemplateDoesNotExist:
            raise Http404
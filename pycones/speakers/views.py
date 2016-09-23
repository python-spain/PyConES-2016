# -*- coding: utf-8 -*-
from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View

from speakers.forms import SpeakerForm


class EditSpeaker(LoginRequiredMixin, View):
    """View for edit the speaker information."""

    @staticmethod
    def get(request):
        try:
            form = SpeakerForm(instance=request.user.speaker_profile)
        except ObjectDoesNotExist:
            raise Http404
        data = {
            "form": form
        }
        return render(request, "speakers/edit.html", data)

    @staticmethod
    def post(request):
        try:
            form = SpeakerForm(request.POST, request.FILES, instance=request.user.speaker_profile)
        except ObjectDoesNotExist:
            raise Http404
        data = {
            "form": form
        }
        if form.is_valid():
            form.save()
            messages.success(request, _("Datos actualizados correctamente"))
            return redirect(reverse("speakers:edit"))
        return render(request, "speakers/edit.html", data)

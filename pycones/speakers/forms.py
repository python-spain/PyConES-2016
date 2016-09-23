# -*- coding: utf-8 -*-
from django import forms

from speakers.models import Speaker


class SpeakerForm(forms.ModelForm):

    class Meta:
        model = Speaker
        fields = ["biography", "photo"]
        widgets = {
            "biography": forms.Textarea(attrs={"class": "form-control"})
        }

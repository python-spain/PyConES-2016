# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from reviewers.models import Review


class SignInForm(forms.Form):
    """Form for handle in a user can log in."""

    username = forms.fields.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": _("Nombre de usuario"),
            "autocapitalize": "off",
            "autocorrect": "off",
            "autofocus": "autofocus",
        }),
        error_messages={'required': _('El nombre de usuario es obligatorio')}
    )
    password = forms.fields.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": _("Contraseña")
        }),
        error_messages={'required': _('La contraseña es obligatoria')}
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(_("Nombre de usuario no encontrado"))
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise forms.ValidationError(_("La contraseña no es correcta"))
        except User.DoesNotExist:
            pass
        return password


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["relevance", "interest", "newness", "notes", "conflict", "finished"]
        widgets = {
            "relevance": forms.NumberInput(attrs={"class": "form-control"}),
            "interest": forms.NumberInput(attrs={"class": "form-control"}),
            "newness": forms.NumberInput(attrs={"class": "form-control"}),
            "notes": forms.Textarea(attrs={"class": "form-control"}),
        }

    @staticmethod
    def _clean_metric(metric):
        if metric is None:
            return metric
        if 0 >= metric or metric > 10:
            raise forms.ValidationError(_("Debes puntuar entre 1 y 10"))
        return metric

    def clean_interest(self):
        interest = self.cleaned_data.get("interest")
        return self._clean_metric(interest)

    def clean_relevance(self):
        relevance = self.cleaned_data.get("relevance")
        return self._clean_metric(relevance)

    def clean_newness(self):
        newness = self.cleaned_data.get("newness")
        return self._clean_metric(newness)

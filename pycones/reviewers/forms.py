# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Review, Reviewer


class SignInForm(forms.Form):
    """Form for handle in a user can log in."""

    username = forms.fields.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": _("Email o nombre de usuario"),
            "autocapitalize": "off",
            "autocorrect": "off",
            "autofocus": "autofocus",
        }),
        error_messages={'required': _('El email o nombre de usuario es obligatorio')}
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
        email_validator = forms.EmailField()
        try:
            email = email_validator.clean(username)
            if User.objects.filter(email=email).exists():
                username = User.objects.get(email=email).username
                return username
            else:
                raise forms.ValidationError(_("Email no encontrado"))
        except ValidationError:
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
            "relevance": forms.NumberInput(attrs={"class": "form-control", 
                                                  "min": "1", "max": "10", "step": "1"}),
            "interest": forms.NumberInput(attrs={"class": "form-control", 
                                                 "min": "1", "max": "10", "step": "1"}),
            "newness": forms.NumberInput(attrs={"class": "form-control", 
                                                "min": "1", "max": "10", "step": "1"}),
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


class RestorePasswordForm(forms.Form):

    email = forms.EmailField(label=_("Email"), widget=forms.HiddenInput())
    restore_code = forms.CharField(widget=forms.HiddenInput())
    password = forms.CharField(label=_("Contraseña"), widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": _("Contraseña"),
        }
    ))
    repeat_password = forms.CharField(label=_("Repita la contraseña"), widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": _("Repita la contraseña"),
        }
    ))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not Reviewer.objects.filter(user__email=email).exists():
            raise forms.ValidationError(_("El email no existe"))
        return email

    def clean_repeat_password(self):
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("repeat_password")
        if password != repeat_password:
            raise forms.ValidationError(_("Las contraseñas no son iguales"))
        return repeat_password

    def clean_restore_code(self):
        email = self.cleaned_data.get("email")
        restore_code = self.cleaned_data.get("restore_code")
        if not Reviewer.objects.filter(user__email=email).exists():
            raise forms.ValidationError(_("Código de restauración no válido"))
        reviewer = Reviewer.objects.get(user__email=email)
        if reviewer.restore_code != restore_code:
            raise forms.ValidationError(_("Código de restauración no válido"))
        return restore_code


class RequestRestoreCodeForm(forms.Form):

    email = forms.EmailField(label=_("Email"), widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": _("Email"),
    }))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not Reviewer.objects.filter(user__email=email).exists():
            raise forms.ValidationError(_("El email no pertenece a un revisor"))
        return email

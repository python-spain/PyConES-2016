# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned
from django.utils.translation import ugettext_lazy as _
from markupfield.widgets import AdminMarkupTextareaWidget

from speakers.models import Speaker


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
        if not Speaker.objects.filter(user__email=email).exists():
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
        if not Speaker.objects.filter(user__email=email).exists():
            raise forms.ValidationError(_("Código de restauración no válido"))
        reviewer = Speaker.objects.get(user__email=email)
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
        if not Speaker.objects.filter(user__email=email).exists():
            raise forms.ValidationError(_("El email no pertenece a un revisor"))
        return email


class SignInForm(forms.Form):
    """Form for handle in a user can log in."""

    username = forms.fields.CharField(
        label=_("Nombre de usuario o email"),
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
        label=_("Contraseña"),
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
        except MultipleObjectsReturned:
            email = email_validator.clean(username)
            speakers = Speaker.objects.filter(user__email=email)
            if not speakers.exists():
                raise forms.ValidationError(_("Email no encontrado"))
            elif speakers.count() > 1:
                raise forms.ValidationError(_("Este email no se puede usar para acceder al sistema"))
        except forms.ValidationError:
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


class SpeakerForm(forms.ModelForm):

    class Meta:
        model = Speaker
        fields = ["name", "biography", "photo"]
        widgets = {
            "biography": AdminMarkupTextareaWidget(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv

from django import forms
from django.utils.translation import ugettext_lazy as _

from attendees.models import Attendee


class ImportAttendeeForm(forms.Form):
    """Form to import data of attendees at the admin page."""
    file = forms.FileField()

    def save(self):
        """Reads CSV uploaded file and creates attendees models."""
        uploaded_file = self.cleaned_data.get("file")
        uploaded_file_content = uploaded_file.read()
        uploaded_file_content = uploaded_file_content.decode("utf-8")
        uploaded_file_content = map(lambda item: item.strip(), uploaded_file_content.split("\n"))
        reader = csv.DictReader(uploaded_file_content, delimiter=";")
        for row in reader:
            attendees = Attendee.objects.filter(tracker=row["Localizador"])
            if not attendees.exists():
                attendee = Attendee.objects.create(
                    name=row["Nombre"],
                    email=row["E-mail"],
                    barcode=row['Código de barras'] if row['Código de barras'] else None,
                    tracker=row["Localizador"],
                )
                attendee.create_user()
            else:
                attendee = attendees.first()
                attendee.create_user()
            if not attendee.restore_code:
                attendee.generate_restore_code()


class RestorePasswordForm(forms.Form):

    tracker = forms.CharField(label=_("Localizador"), widget=forms.HiddenInput())
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

    def clean_tracker(self):
        tracker = self.cleaned_data.get("tracker")
        if not Attendee.objects.filter(tracker=tracker).exists():
            raise forms.ValidationError(_("El localzador de entrada no existe"))
        return tracker

    def clean_repeat_password(self):
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("repeat_password")
        if password != repeat_password:
            raise forms.ValidationError(_("Las contraseñas no son iguales"))
        return repeat_password

    def clean_restore_code(self):
        tracker = self.cleaned_data.get("tracker")
        restore_code = self.cleaned_data.get("restore_code")
        if not Attendee.objects.filter(tracker=tracker).exists():
            raise forms.ValidationError(_("Código de restauración no válido"))
        attendee = Attendee.objects.get(tracker=tracker)
        if attendee.restore_code != restore_code:
            raise forms.ValidationError(_("Código de restauración no válido"))
        return restore_code


class RequestRestoreCodeForm(forms.Form):

    tracker = forms.CharField(label=_("Localizador"), widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": _("Localizador de entrada"),
    }))

    def clean_tracker(self):
        tracker = self.cleaned_data.get("tracker")
        if not Attendee.objects.filter(tracker=tracker).exists():
            raise forms.ValidationError(_("El localzador de entrada no existe"))
        return tracker


class AttendeeSigInForm(forms.Form):

    tracker = forms.CharField(label=_("Localizador"), widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": _("Localizador de entrada"),
    }))
    password = forms.CharField(label=_("Contraseña"), widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": _("Contraseña"),
        }
    ))

    def clean_tracker(self):
        tracker = self.cleaned_data.get("tracker")
        if not Attendee.objects.filter(tracker=tracker).exists():
            raise forms.ValidationError(_("El localzador de entrada no existe"))
        return tracker

    def clean_password(self):
        tracker = self.cleaned_data.get("tracker")
        password = self.cleaned_data.get("password")
        if not Attendee.objects.filter(tracker=tracker).exists():
            raise forms.ValidationError(_("La contraseña no es correcta"))
        attendee = Attendee.objects.filter(tracker=tracker).first()
        if not attendee.user:
            raise forms.ValidationError(_("La contraseña no es correcta"))
        if not attendee.user.check_password(password):
            raise forms.ValidationError(_("La contraseña no es correcta"))
        return password


class AttendeeForm(forms.ModelForm):

    class Meta:
        model = Attendee
        exclude = ("user", "barcode", "tracker", "restore_code", "notes")
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "readonly": "readonly"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "readonly": "readonly"
            }),
            "dni": forms.TextInput(attrs={
                "class": "form-control",
                "readonly": "readonly"
            }),
            "allergies": forms.Textarea(attrs={
                "class": "form-control",
                "readonly": "readonly"
            }),
        }


class AdminAttendeeForm(forms.ModelForm):

    class Meta:
        model = Attendee
        fields = "__all__"

    def clean_dni(self):
        dni = self.cleaned_data.get("dni")
        if not dni:
            return None
        return dni

    def clean_barcode(self):
        barcode = self.cleaned_data.get("barcode")
        if not barcode:
            return None
        return barcode

    def clean_restore_code(self):
        restore_code = self.cleaned_data.get("restore_code")
        if not restore_code:
            return None
        return restore_code

    def clean_tracker(self):
        tracker = self.cleaned_data.get("tracker")
        if not tracker:
            return None
        return tracker

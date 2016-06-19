# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models
from django.template import Context
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from core.helpers.email import send_template_email
from core.helpers.generators import random_string


class Attendee(TimeStampedModel):
    """Attendee to the event, with fields imported from
    Ticketea.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)

    name = models.CharField(verbose_name=_("Nombre completo y apellidos"), max_length=128, null=True, blank=True)
    email = models.EmailField(verbose_name=_("Email"), max_length=128, null=True, blank=True)
    dni = models.CharField(verbose_name=_("DNI"), max_length=16, unique=True, null=True, blank=True, default=None)
    barcode = models.CharField(max_length=32, unique=True, null=True, blank=True)
    tracker = models.CharField(
        max_length=16, unique=True, null=True, blank=True, verbose_name=_("localizador ticketea")
    )
    restore_code = models.CharField(max_length=16, null=True, blank=True, unique=True)
    notes = models.TextField(verbose_name=_("Notas"), null=True, blank=True)
    allergies = models.TextField(
        verbose_name=_("Consideraciones para el catering"), null=True, blank=True,
        help_text=_("Alergias, dieta especial o cualquier cosas que quieres que tengamos en cuenta para el catering. "
                    "Se hará lo posible por ajustarse a las necesidades particulares.")
    )
    workshop_attendance = models.NullBooleanField(
        verbose_name=_("¿Vas a asistir a los talleres del viernes?"), null=True, blank=True
    )

    def create_user(self):
        """Creates user in case the is no user associated with this
        attendee.
        """
        if self.user is None:
            users = User.objects.filter(username=self.tracker)
            if users.exists():
                self.user = users.first()
            else:
                self.user = User.objects.create_user(
                    username=self.tracker, email=self.email, password=random_string(),
                    first_name=self.name.split(" ")[0], last_name=" ".join(self.name.split(" ")[1:])
                )
            self.save()
        return self.user

    def generate_restore_code(self):
        self.restore_code = random_string(16)
        self.save()

    def restore_password_link(self):
        return reverse("attendees:restore_password", kwargs={"restore_code": self.restore_code})

    def send_restore_password_link(self):
        """Sends email with link to restore password."""
        if not self.restore_code:
            self.generate_restore_code()
        context = Context({
            "attendee": self,
        })
        send_template_email(
            _("Establece tu contraseña"),
            "PyConES 2015 <contacto2015@es.pycon.org>",
            self.email,
            "attendees/restore_email.html",
            context
        )

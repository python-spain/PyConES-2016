# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.templatetags.static import static
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from markupfield.fields import MarkupField
from model_utils.models import TimeStampedModel

from core.helpers.email import send_template_email
from core.helpers.generators import random_string


@python_2_unicode_compatible
class Speaker(TimeStampedModel):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, related_name="speaker_profile")
    name = models.CharField(
        verbose_name=_("Nombre"),
        max_length=100, help_text=("As you would like it to appear in the "
                                                       "conference program."))
    biography = MarkupField(
        verbose_name=_("Biografía"),
        blank=True,
        default="",
        default_markup_type='markdown',
        help_text=("A little bit about you.  Edit using "
                   "<a href='http://warpedvisions.org/projects/"
                   "markdown-cheat-sheet/target='_blank'>"
                   "Markdown</a>.")
    )
    photo = models.ImageField(verbose_name=_("Foto"), upload_to="speaker_photos", blank=True)
    annotation = models.TextField()  # staff only
    is_keynoter = models.BooleanField(default=False)
    restore_code = models.CharField(max_length=16, null=True, blank=True, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        if self.user:
            return self.name
        else:
            return "?"

    @property
    def photo_url(self):
        try:
            return self.photo.url
        except ValueError:
            return static("img/default-avatar.png")

    @property
    def email(self):
        if self.user is not None:
            return self.user.email
        else:
            return self.invite_email

    @property
    def all_presentations(self):
        presentations = []
        if self.presentations:
            for p in self.presentations.all():
                presentations.append(p)
            for p in self.copresentations.all():
                presentations.append(p)
        return presentations

    def has_biography(self):
        return bool(self.biography.raw)

    def get_api_id(self):
        return "S{:05d}".format(self.pk)

    def generate_restore_code(self):
        self.restore_code = random_string(16)
        self.save()

    def restore_password_link(self):
        return reverse("speakers:restore_password", kwargs={"restore_code": self.restore_code})

    def send_restore_password_link(self):
        """Sends email with link to restore password."""
        if not self.restore_code:
            self.generate_restore_code()
        context = {
            "speaker": self,
        }
        send_template_email(
            subject=_("[PyConES 2016] Establece tu contraseña"),
            from_email="PyConES 2016 <contacto2016@es.pycon.org>",
            to=self.user.email,
            template_name="emails/speakers/restore_email.html",
            context=context
        )

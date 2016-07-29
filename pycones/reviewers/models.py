# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models
from django.template import Context
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from configurations.models import Option
from core.emails import send_email

from core.helpers.email import send_template_email
from core.helpers.generators import random_string


class Review(TimeStampedModel):
    """A review assignation. A review user have assigned a proposal to
    review."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="reviews")
    proposal = models.ForeignKey("proposals.Proposal", related_name="reviews")

    relevance = models.PositiveIntegerField(
        verbose_name=_("Relevancia"), null=True, blank=True, help_text=_("Puntuación del 1 al 10")
    )
    interest = models.PositiveIntegerField(
        verbose_name=_("Interés General"), null=True, blank=True, help_text=_("Puntuación del 1 al 10")
    )
    newness = models.PositiveIntegerField(
        verbose_name=_("Novedad"), null=True, blank=True, help_text=_("Puntuación del 1 al 10")
    )

    notes = models.TextField(verbose_name=_("Notas del revisor"), blank=True, null=True)

    conflict = models.BooleanField(verbose_name=_("¿Existe un conflico de intereses?"), default=False)
    finished = models.BooleanField(verbose_name=_("¿Revisión finalizada?"), default=False)

    class Meta:
        unique_together = ["user", "proposal"]

    def avg(self):
        data = [self.relevance, self.interest, self.newness]
        weights = [
            Option.objects.get_value("{}_weights".format(name), 1.0) for name in ("relevance", "interest", "newness")
        ]
        if None not in data:
            data = zip(data, weights)
            return sum([attr * weight for attr, weight in data]) / sum(weights)
        return None

    def notify(self):
        context = {
            "site": Site.objects.get_current(),
            "first_name": self.user.first_name,
            "title": self.proposal.title,
        }
        send_email(
            context=context,
            template="emails/reviewers/new.html",
            subject=_("[PyConES 2016] Tienes una nueva propuesta para revisar"),
            to=self.user.email,
            from_email="PyConES 2016 <contacto2016@es.pycon.org>"
        )

    def save(self, **kwargs):
        is_insert = self.pk is None
        old_user = None
        if not is_insert:
            old_user = Review.objects.get(pk=self.pk).user
        super(Review, self).save(**kwargs)
        if is_insert or self.user != old_user:
            self.notify()


class Reviewer(TimeStampedModel):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    restore_code = models.CharField(max_length=16, null=True, blank=True, unique=True)

    def reviews_count(self):
        return self.user.reviews.count()

    def generate_restore_code(self):
        self.restore_code = random_string(16)
        self.save()

    def restore_password_link(self):
        return reverse("reviewers:restore_password", kwargs={"restore_code": self.restore_code})

    def send_restore_password_link(self):
        """Sends email with link to restore password."""
        if not self.restore_code:
            self.generate_restore_code()
        context = {
            "reviewer": self,
        }
        send_template_email(
            subject=_("[PyConES 2016] Establece tu contraseña"),
            from_email="PyConES 2016 <contacto2016@es.pycon.org>",
            to=self.user.email,
            template_name="emails/reviewers/restore_email.html",
            context=context
        )

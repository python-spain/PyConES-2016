# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import uuid

import numpy as np
import reversion
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from markupfield.fields import MarkupField
from model_utils.managers import InheritanceManager

from taggit_autosuggest.managers import TaggableManager

from core.emails import send_email
from core.helpers.generators import random_string

from reviewers.models import Reviewer


@python_2_unicode_compatible
class ProposalSection(models.Model):
    """
    configuration of proposal submissions for a specific Section.

    a section is available for proposals iff:
      * it is after start (if there is one) and
      * it is before end (if there is one) and
      * closed is NULL or False
    """

    section = models.OneToOneField("conference.Section")

    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    closed = models.NullBooleanField()
    published = models.NullBooleanField()

    @classmethod
    def available(cls):
        return cls._default_manager.filter(
            Q(start__lt=now()) | Q(start=None),
            Q(end__gt=now()) | Q(end=None),
            Q(closed=False) | Q(closed=None),
        )

    def is_available(self):
        if self.closed:
            return False
        if self.start and self.start > now():
            return False
        if self.end and self.end < now():
            return False
        return True

    def __str__(self):
        return self.section.name


@python_2_unicode_compatible
class ProposalKind(models.Model):
    """
    e.g. talk vs panel vs tutorial vs poster

    Note that if you have different deadlines, reviewers, etc. you'll want
    to distinguish the section as well as the kind.
    """

    section = models.ForeignKey("conference.Section", related_name="proposal_kinds")

    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ProposalBase(models.Model):
    objects = InheritanceManager()

    kind = models.ForeignKey(ProposalKind, verbose_name=_("Tipo de propuesta"))

    title = models.CharField(max_length=100, verbose_name=_("Título"))
    description = models.TextField(
        _("Breve descripción"),
        max_length=500,
        help_text=_("If your proposal is accepted this will be made public and printed in the "
                    "program. Should be one paragraph, maximum 500 characters.")
    )
    abstract = MarkupField(
        _("Resumen detallado"),
        blank=True,
        default="",
        default_markup_type='markdown',
        help_text=_("Detailed outline. Will be made public if your proposal is accepted. Edit "
                    "using <a href='http://daringfireball.net/projects/markdown/basics' "
                    "target='_blank'>Markdown</a>.")
    )
    additional_notes = MarkupField(
        _("Notas adicionales"),
        blank=True,
        default="",
        default_markup_type='markdown',
        help_text=_("Anything else you'd like the program committee to know when making their "
                    "selection: your past experience, etc. If it's a workshop, specify the duration. This is not made "
                    "public. Edit using "
                    "<a href='http://daringfireball.net/projects/markdown/basics' "
                    "target='_blank'>Markdown</a>.")
    )

    submitted = models.DateTimeField(
        default=now,
        editable=False,
    )
    speaker = models.ForeignKey("speakers.Speaker", related_name="proposals")
    additional_speakers = models.ManyToManyField("speakers.Speaker", through="AdditionalSpeaker",
                                                 blank=True)
    cancelled = models.BooleanField(default=False)
    notified = models.BooleanField(default=False)
    accepted = models.NullBooleanField(verbose_name=_('Aceptada'), default=None)
    accepted_notified = models.BooleanField(verbose_name=_('Notificación de aceptación enviada'), default=False)
    code = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return "%s - %s" % (self.pk, self.title)

    @property
    def section(self):
        return self.kind.section

    @property
    def speaker_email(self):
        return self.speaker.email

    @property
    def number(self):
        return str(self.pk).zfill(3)

    @staticmethod
    def can_edit():
        return True

    def speakers(self):
        yield self.speaker
        speakers = self.additional_speakers.exclude(
            additionalspeaker__status=AdditionalSpeaker.SPEAKING_STATUS_DECLINED)
        for speaker in speakers:
            yield speaker

    def notification_email_context(self):
        site = Site.objects.get_current()
        return {
            "title": self.title,
            "speaker": self.speaker.name,
            "kind": self.kind.name,
            "code": self.code,
            "site": site,
        }

    def notify(self):
        """Sends an email to the creator of the proposal with a confirmation email. The emails has a
        link to edit the proposal.
        """
        if not self.code:
            self.code = random_string(64)
        context = self.notification_email_context()
        send_email(
            context=context,
            template="emails/proposals/confirmation.html",
            subject=_("[PyConES 2016] Confirmación de propuesta de charla"),
            to=self.speaker.email,
            from_email="contacto2016@es.pycon.org"
        )
        self.notified = True
        self.save()

    def notify_acceptance(self):
        """Sends an email to the creator of the proposal with an email with the resolution of the acceptance or not
        of his proposal.
        """
        context = self.notification_email_context()
        if self.accepted is None:
            return
        template = "emails/proposals/accepted.html" if self.accepted else "emails/proposals/rejected.html"
        send_email(
            context=context,
            template=template,
            subject=_("[PyConES 2016] Notificación de propuesta de charla"),
            to=self.speaker.email,
            from_email="contacto2016@es.pycon.org"
        )
        self.accepted_notified = True
        self.save()


reversion.register(ProposalBase)


class Proposal(ProposalBase):
    BASIC_LEVEL, INTERMEDIATE_LEVEL, ADVANCED_LEVEL = "basic", "intermediate", "advanced"
    PROPOSAL_LEVELS = (
        (BASIC_LEVEL, _("Básico")),
        (INTERMEDIATE_LEVEL, _("Intermedio")),
        (ADVANCED_LEVEL, _("Avanzado")),
    )
    PROPOSAL_LANGUAGES = (
        ("es", _("Español")),
        ("en", _("Inglés")),
    )
    PROPOSAL_DURATIONS = (
        (15, _("15 minutos")),
        (30, _("30 minutos")),
    )
    audience_level = models.CharField(
        verbose_name=_("Nivel de la audiencia"), choices=PROPOSAL_LEVELS, null=True, default=BASIC_LEVEL, max_length=32
    )
    language = models.CharField(
        verbose_name=_("Idioma"), max_length=2, choices=PROPOSAL_LANGUAGES, default="es"
    )
    duration = models.PositiveIntegerField(
        verbose_name=_("Duración"), choices=PROPOSAL_DURATIONS, default=30, null=True, blank=True
    )

    tags = TaggableManager(verbose_name=_("Etiquetas"),
                           help_text=_("Lista de etiquetas separadas por comas."),
                           blank=True)

    @property
    def avg_property(self):
        return self.avg()

    @property
    def completed_reviews_property(self):
        return self.reviews.filter(finished=True).count()

    @property
    def assigned_reviews_property(self):
        return self.reviews.count()

    @property
    def tag_list_property(self):
        return u", ".join(tag.name for tag in self.tags.all())

    @property
    def renormalization_O0_property(self):
        return self.renormalization_O0()

    @property
    def renormalization_O1_property(self):
        return self.renormalization_O1()

    def avg(self):
        data = [review.avg() for review in self.reviews.filter(finished=True) if review.avg() is not None]
        if data:
            return sum(data) / len(data)
        return None

    def renormalization_O0(self):
        """Renormalization with order 0. Average value of 0"""
        relevance, interest, newness = [], [], []
        for review in self.reviews.all():
            reviewer = Reviewer.objects.get(user=review.user)
            mean = reviewer.mean()
            if reviewer.num_reviews() <= 1:
                continue
            relevance.append((review.relevance or 0) - mean)
            interest.append((review.interest or 0) - mean)
            newness.append((review.newness or 0) - mean)
        return np.mean(interest + relevance + newness)

    def renormalization_O1(self):
        """Renormalization with order 1. Expand the value to get the same standard deviation for everyone"""
        relevance, interest, newness = [], [], []
        for review in self.reviews.all():
            reviewer = Reviewer.objects.get(user=review.user)
            std = reviewer.std()
            if reviewer.num_reviews() <= 1 or std < 0.75:
                continue
            relevance.append((review.relevance or 0) - std)
            interest.append((review.interest or 0) - std)
            newness.append((review.newness or 0) - std)
        return np.mean(interest + relevance + newness)


class AdditionalSpeaker(models.Model):
    SPEAKING_STATUS_PENDING = 1
    SPEAKING_STATUS_ACCEPTED = 2
    SPEAKING_STATUS_DECLINED = 3

    SPEAKING_STATUS = [
        (SPEAKING_STATUS_PENDING, _("Pending")),
        (SPEAKING_STATUS_ACCEPTED, _("Accepted")),
        (SPEAKING_STATUS_DECLINED, _("Declined")),
    ]

    speaker = models.ForeignKey("speakers.Speaker")
    proposalbase = models.ForeignKey(ProposalBase)
    status = models.IntegerField(choices=SPEAKING_STATUS, default=SPEAKING_STATUS_PENDING)

    class Meta:
        unique_together = ("speaker", "proposalbase")


def uuid_filename(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("document", filename)


class SupportingDocument(models.Model):
    proposal = models.ForeignKey(ProposalBase, related_name="supporting_documents")

    uploaded_by = models.ForeignKey(User)

    created_at = models.DateTimeField(default=now)

    file = models.FileField(upload_to=uuid_filename)
    description = models.CharField(max_length=140)

    def download_url(self):
        return reverse("proposal_document_download",
                       args=[self.pk, os.path.basename(self.file.name).lower()])

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from configurations.managers import OptionManager


@python_2_unicode_compatible
class Option(models.Model):
    """System options and configurations."""

    FLOAT, INT, STRING = (0, 1, 2)
    TYPE_CHOICES = (
        (FLOAT, _("Float")),
        (INT, _("Integer")),
        (STRING, _("String")),
    )
    name = models.CharField(
        verbose_name=_("Parameter"),
        max_length=255,
        unique=True,
        db_index=True
    )
    public_name = models.CharField(
        verbose_name=_("Public name of the parameter"),
        max_length=255,
        unique=False,
        db_index=True
    )
    type = models.PositiveIntegerField(
        choices=TYPE_CHOICES,
        default=STRING
    )
    value = models.CharField(
        null=True,
        blank=True,
        default=None,
        max_length=256,
        verbose_name=_("Value")
    )

    is_list = models.BooleanField(default=False)

    objects = OptionManager()

    def __str__(self):
        return "%s" % self.public_name

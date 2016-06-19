# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Section(models.Model):

    name = models.CharField(_("name"), max_length=100)
    slug = models.SlugField()

    start_date = models.DateField(_("start date"), null=True, blank=True)
    end_date = models.DateField(_("end date"), null=True, blank=True)

    class Meta(object):
        verbose_name = _("section")
        verbose_name_plural = _("sections")
        ordering = ["start_date"]

    def __str__(self):
        return "%s" % self.name

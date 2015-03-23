# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify
from django.utils.translation import ugettext as _
from django_extensions.db.models import TimeStampedModel
from markupfield.fields import MarkupField

from blog.managers import ArticlesManager
from core.helpers.files import UploadToDir


class AbstractArticle(TimeStampedModel):
    """Abstract model for articles, posts, etc."""
    DRAFT, SCHEDULED, PUBLISHED = (0, 1, 2)
    STATUSES = (
        (DRAFT, _("Draft")),
        (SCHEDULED, _("Scheduled")),
        (PUBLISHED, _("Published")),
    )

    status = models.PositiveIntegerField(choices=STATUSES, default=DRAFT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.TextField()
    slug = models.SlugField(blank=True, unique=True)
    content = MarkupField(default="", blank=True)

    scheduled_at = models.DateTimeField(null=True, blank=True)

    outstanding_image = models.ImageField(upload_to=UploadToDir('images', random_name=False), null=True, blank=True)

    objects = ArticlesManager()

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Post(AbstractArticle):
    """Post for blogging"""
    tags = models.ManyToManyField("blog.Tag", related_name="posts", blank=True)

    def __str__(self):
        return self.title

    def _read_more_tag(self):
        """
        <p><a href="{% url "post" slug=post.slug %}">{% trans "Seguir leyendo..." %}</a></p>
        @return:
        """
        return u'<p><a href="{}">{}</a></p>'.format(
            reverse("post", kwargs={'slug': self.slug}),
            _(u"Seguir leyendo...")
        )

    def summary(self):
        """Split content using <!--more-->"""
        split_content = self.content.split(u"<!--more-->")
        read_more = self._read_more_tag() if len(split_content) > 1 else u""
        return u"{}{}".format(
            split_content[0],
            read_more
        )

    def save(self, *args, **kwargs):
        slug_base = self.slug if self.slug else self.title
        self.slug = slugify(slug_base)
        super(Post, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Tag(models.Model):
    """Tag for posts."""

    name = models.CharField(max_length=128)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slug_base = self.slug if self.slug else self.name
        self.slug = slugify(slug_base)
        super(Tag, self).save(*args, **kwargs)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models


class ArticlesManager(models.Manager):
    """Manager for posts. handle articles."""

    def requested_objects(self, request, page=None, queryset=None):
        if not queryset:
            queryset = self.all()
        posts_list = queryset.filter(status=self.model.PUBLISHED).order_by('-created')
        paginator = Paginator(posts_list, 5)
        if page is None:
            page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return posts

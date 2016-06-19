# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from blog.views import PostsListView, PostDetailsView, PostsTagListView, PostsFeed, PostsAtomFeed

urlpatterns = [
    url(r'^$', PostsListView.as_view(), name="list"),
    url(r'^feed/', PostsFeed(), name="blog_feed"),
    url(r'^atom/', PostsAtomFeed(), name="blog_atom"),
    url(r'^rss/', RedirectView.as_view(url=reverse_lazy('blog_feed'))),
    url(r'^tag/(?P<slug>.+)/$', PostsTagListView.as_view(), name="posts_tag"),
    url(r'^(?P<slug>.+)/$', PostDetailsView.as_view(), name="post"),
]

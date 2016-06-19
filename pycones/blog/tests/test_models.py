# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils.text import slugify
from model_mommy import mommy

from blog.models import Post


class PostModelTests(TestCase):

    def setUp(self):
        self.user_password = "pass"
        self.user = mommy.make('auth.User', email='user@example.com')
        self.user.set_password(self.user_password)
        self.user.save()

    def _create_post(self, content="foo"):
        return Post.objects.create(
            author=self.user,
            content=content,
            title="Title",
            slug="Title",
            content_markup_type='markdown'
        )

    def test_create_post(self):
        prev_posts = Post.objects.count()
        self._create_post()
        self.assertEqual(prev_posts + 1, Post.objects.count())

    def test_create_slug(self):
        post = mommy.make('blog.Post', author=self.user, content_markup_type='markdown')
        post.save()
        self.assertEqual(post.slug, slugify(post.title))

    def test_more(self):
        original_summary = "part1"
        post = self._create_post("{}<!--more-->more".format(original_summary))
        summary = post.summary()
        self.assertEqual(summary, '{}<p><a href="/es/blog/title/">Seguir leyendo...</a></p>'.format(original_summary))
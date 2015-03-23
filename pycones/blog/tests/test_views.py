# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.test import TestCase
from model_mommy import mommy
from blog.models import Post


class BlogViewTests(TestCase):
    def setUp(self):
        self.user_password = "pass"
        self.user = mommy.make('auth.User', email='user@example.com')
        self.user.set_password(self.user_password)
        self.user.save()

    def test_blog(self):
        mommy.make('blog.Post', author=self.user, content_markup_type='markdown', _quantity=5)
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)

    def test_blog_tags(self):
        tag = mommy.make('blog.Tag')
        mommy.make('blog.Post', author=self.user, tags=[tag], content_markup_type='markdown', _quantity=5)
        response = self.client.get(reverse('posts_tag', kwargs={'slug': tag.slug}))
        self.assertEqual(response.status_code, 200)

    def test_blog_feed(self):
        mommy.make('blog.Post', author=self.user, content_markup_type='markdown', _quantity=5)
        response = self.client.get(reverse('blog_feed'))
        self.assertEqual(response.status_code, 200)

    def test_blog_atom(self):
        mommy.make('blog.Post', author=self.user, content_markup_type='markdown', _quantity=5)
        response = self.client.get(reverse('blog_atom'))
        self.assertEqual(response.status_code, 200)

    def test_blog_details(self):
        post = Post.objects.create(author=self.user, title="Title", slug="slug", content_markup_type='markdown', status=Post.PUBLISHED)
        response = self.client.get(reverse('post', kwargs={'slug': post.slug}))
        self.assertEqual(response.status_code, 200)

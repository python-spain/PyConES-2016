# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm, TextInput
from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'status']
    list_filter = ('status', )


admin.site.register(Post, PostAdmin)
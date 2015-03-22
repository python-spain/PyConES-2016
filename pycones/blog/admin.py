# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm, TextInput
from django.contrib import admin

from blog.models import Post


class PostForm(ModelForm):

    class Meta:
        widgets = {
            'title': TextInput(),
            'content': TextInput()
        }


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'status']
    list_filter = ('status', )
    form = PostForm
    fieldsets = [
        (None, {'fields': ('title', 'slug', 'author', 'status', 'outstanding_image')}),
        ('Dates', {'fields': ('created', 'scheduled_at',)}),
        ('Tags', {'fields': ('tags', )}),
        ('Content', {'classes': ('full-width',), 'fields': ('content',)}),
    ]


admin.site.register(Post, PostAdmin)
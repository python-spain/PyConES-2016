# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

from django.contrib import admin
from markupfield.widgets import AdminMarkupTextareaWidget

from blog.models import Post


class PostAdminForm(forms.ModelForm):

    class Meta:
        widgets = {
            'title': forms.Textarea(attrs={'class': 'span12'}),
            'title_en': forms.Textarea(attrs={'class': 'span12'}),
            'title_es': forms.Textarea(attrs={'class': 'span12'}),
            'content': AdminMarkupTextareaWidget(attrs={'class': 'span12'}),
            'content_es': AdminMarkupTextareaWidget(attrs={'class': 'span12'}),
            'content_en': AdminMarkupTextareaWidget(attrs={'class': 'span12'}),
        }


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'status']
    list_filter = ('status', )
    form = PostAdminForm


admin.site.register(Post, PostAdmin)

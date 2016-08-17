# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from reviewers import review_group_name
from reviewers.models import Review, Reviewer

from .actions import export_as_csv_action


class ReviewAdminForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ReviewAdminForm, self).__init__(*args, **kwargs)
        self.fields["user"].queryset = get_user_model().objects.filter(
            Q(groups__name=review_group_name) | Q(is_superuser=True)
        )

    def clean(self):
        cleaned_data = super(ReviewAdminForm, self).clean()
        user = cleaned_data.get("user")
        proposal = cleaned_data.get("proposal")
        if user == proposal.speaker.user:
            raise forms.ValidationError("You can not asign a review to its author!")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "proposal", "user", "relevance", "interest", "newness", "get_avg", "conflict", "finished",
                    "created"]
    list_filter = ["proposal", "user", "conflict", "finished"]

    actions = [
        export_as_csv_action("CSV Export", fields=[
            "id",
            "proposal",
            "user",
            "relevance",
            "interest",
            "newness",
            "avg_property",
            "conflict",
            "finished",
            "created",
        ])
    ]

    form = ReviewAdminForm

    def get_avg(self, instance):
        return instance.avg()
    get_avg.short_description = _("Media")


@admin.register(Reviewer)
class ReviewerAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "get_reviews", "created"]

    def get_reviews(self, instance):
        return instance.reviews_count()
    get_reviews.short_description = _("Revisiones")
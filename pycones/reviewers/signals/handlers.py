# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import
from django.contrib.auth import get_user_model
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from reviewers import review_group_name
from reviewers.models import Reviewer

user_model = get_user_model()


@receiver(m2m_changed, sender=user_model.groups.through)
def register_reviews_handler(sender, **kwargs):
    action = kwargs.get("action")
    instance = kwargs.get("instance")
    if instance and action in ("post_add", "post_remove"):
        if review_group_name in instance.groups.values_list("name", flat=True):
            if not Reviewer.objects.filter(user=instance).exists():
                Reviewer.objects.create(user=instance)
        else:
            if Reviewer.objects.filter(user=instance).exists():
                Reviewer.objects.filter(user=instance).delete()

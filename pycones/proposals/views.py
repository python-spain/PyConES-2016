# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from blog.models import Post
from configurations.models import Option

from proposals.forms import ProposalFrom


class SubmitProposalView(View):
    """View to submit proposals."""

    @staticmethod
    def get_more_info_link():
        try:
            post_pk = Option.objects.get_value("submit_proposal_post_pk", 2)
            more_info_link = Post.objects.get(pk=post_pk).get_absolute_url()
        except Post.DoesNotExist:
            return ""
        return more_info_link

    def get(self, request):
        is_submit_proposal_opened = bool(Option.objects.get_value("submit_proposal_opened", 1))
        if is_submit_proposal_opened:
            form = ProposalFrom()
            data = {
                "form": form,
                "more_info_link": self.get_more_info_link()
            }
            return render(request, "proposals/create.html", data)
        return render(request, "proposals/close.html")

    def post(self, request):
        is_submit_proposal_opened = bool(Option.objects.get_value("submit_proposal_opened", 1))
        if not is_submit_proposal_opened:
            return render(request, "proposals/close.html")
        form = ProposalFrom(request.POST)
        data = {
            "form": form,
            "more_info_link": self.get_more_info_link()
        }
        if form.is_valid():
            form.save()
            return redirect("proposals:success")
        return render(request, "proposals/create.html", data)

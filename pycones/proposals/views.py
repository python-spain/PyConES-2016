# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from blog.models import Post

from proposals.forms import ProposalFrom


class SubmitProposalView(View):
    """View to submit proposals."""

    @staticmethod
    def get_more_info_link():
        try:
            more_info_link = Post.objects.get(pk=2).get_absolute_url()
        except Post.DoesNotExist:
            return ""
        return more_info_link

    def get(self, request):
        form = ProposalFrom()
        data = {
            "form": form,
            "more_info_link": self.get_more_info_link()
        }
        return render(request, "proposals/create.html", data)

    def post(self, request):
        form = ProposalFrom(request.POST)
        data = {
            "form": form,
            "more_info_link": self.get_more_info_link()
        }
        if form.is_valid():
            form.save()
            return redirect("proposals:success")
        return render(request, "proposals/create.html", data)

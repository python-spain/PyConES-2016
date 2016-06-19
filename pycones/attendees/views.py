# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from braces.views import LoginRequiredMixin

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.translation import ugettext_lazy as _

from attendees.forms import AttendeeForm, RestorePasswordForm, AttendeeSigInForm, RequestRestoreCodeForm
from attendees.models import Attendee


class EditAttendanceView(LoginRequiredMixin, View):

    @staticmethod
    def get(request):
        """Show form to register an attendee."""
        try:
            attendee = Attendee.objects.get(user=request.user)
        except Attendee.DoesNotExist:
            raise Http404
        form = AttendeeForm(instance=attendee)
        data = {
            "attendee": attendee,
            "form": form
        }
        return render(request, "attendees/profile.html", data)

    @staticmethod
    def post(request):
        """Register an attendee."""
        # try:
        #     attendee = Attendee.objects.get(user=request.user)
        # except Attendee.DoesNotExist:
        #     raise Http404
        # form = AttendeeForm(request.POST, instance=attendee)
        # if form.is_valid():
        #     form.save()
        #     messages.success(request, _("Datos guardados correctamente"))
        # data = {
        #     "attendee": attendee,
        #     "form": form
        # }
        # return render(request, "attendees/profile.html", data)
        return redirect(reverse("attendees:profile"))


class RestorePasswordView(View):

    @staticmethod
    def get(request, restore_code):
        try:
            attendee = Attendee.objects.get(restore_code=restore_code)
        except Attendee.DoesNotExist:
            raise Http404
        data = {
            "attendee": attendee,
            "restore_code": restore_code,
            "form": RestorePasswordForm(initial={"restore_code": restore_code, "tracker": attendee.tracker})
        }
        return render(request, "attendees/restore.html", data)

    @staticmethod
    def post(request, restore_code):
        form = RestorePasswordForm(request.POST)
        try:
            attendee = Attendee.objects.get(restore_code=restore_code)
        except Attendee.DoesNotExist:
            raise Http404
        if form.is_valid():
            user = attendee.user
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            attendee.restore_code = None
            attendee.save()
            messages.success(request, _("Se ha establecido la nueva contraseña"))
        data = {
            "attendee": attendee,
            "restore_code": restore_code,
            "form": form
        }
        return render(request, "attendees/restore.html", data)


class RequestRestorePasswordView(View):

    @staticmethod
    def get(request):
        data = {
            "form": RequestRestoreCodeForm()
        }
        return render(request, "attendees/request_code.html", data)

    @staticmethod
    def post(request):
        form = RequestRestoreCodeForm(request.POST)
        if form.is_valid():
            tracker = form.cleaned_data.get('tracker')
            try:
                attendee = Attendee.objects.get(tracker=tracker)
            except Attendee.DoesNotExist:
                raise Http404
            attendee.send_restore_password_link()
            messages.success(request, _("Se ha enviado un correo a la cuenta con la que compraste la entrada "
                                        "con un enlace para establecer tu contraseña."))
        data = {
            "form": form
        }
        return render(request, "attendees/request_code.html", data)


class AttendeeSignInView(View):

    @staticmethod
    def get(request):
        if request.user.is_authenticated():
            return redirect("attendees:profile")
        data = {
            "form": AttendeeSigInForm()
        }
        return render(request, "attendees/sign_in.html", data)

    @staticmethod
    def post(request):
        form = AttendeeSigInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                tracker=form.cleaned_data.get('tracker'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                return redirect("attendees:profile")
        return render(request, "attendees/sign_in.html", {
            'form': form,
        })


class LogoutView(LoginRequiredMixin, View):

    @staticmethod
    def get(request):
        logout(request)
        return redirect("attendees:sign_in")

# -*- coding: utf-8 -*-
from braces.views import CsrfExemptMixin
from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View

from speakers.forms import SpeakerForm, SignInForm, RestorePasswordForm, RequestRestoreCodeForm
from speakers.models import Speaker


class SignInView(CsrfExemptMixin, View):
    """View to allow  to login users into the platform."""
    template_name = "speakers/sign_in.html"

    @staticmethod
    def get_next_page(request):
        """Gets the page to go after log in."""
        default_redirect = reverse('speakers:edit')
        next_page = request.GET.get('next') or request.POST.get('next')
        return next_page or default_redirect

    def get(self, request):
        data = {
            "form": SignInForm(),
            "next": request.GET.get('next')
        }
        return render(request, self.template_name, data)

    def post(self, request):
        next_page = self.get_next_page(request=request)
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
                request=request
            )
            if user is not None:
                if Speaker.objects.filter(user=user).exists():
                    login(request, user)
                    return redirect(next_page)
                else:
                    messages.error(request, _("El usuario no es un ponente"))
        data = {"form": form, "next": next_page}
        return render(request, self.template_name, data)


class EditSpeaker(LoginRequiredMixin, View):
    """View for edit the speaker information."""

    def get_login_url(self):
        return reverse("speakers:sign-in")

    @staticmethod
    def get_presentations(request):
        speaker = request.user.speaker_profile
        return speaker.presentations.all()

    def get(self, request):
        try:
            form = SpeakerForm(instance=request.user.speaker_profile)
        except ObjectDoesNotExist:
            raise Http404
        data = {
            "form": form,
            "presentations": self.get_presentations(request),
        }
        return render(request, "speakers/edit.html", data)

    def post(self, request):
        try:
            form = SpeakerForm(request.POST, request.FILES, instance=request.user.speaker_profile)
        except ObjectDoesNotExist:
            raise Http404
        data = {
            "form": form,
            "presentations": self.get_presentations(request),
        }
        if form.is_valid():
            form.save()
            messages.success(request, _("Datos actualizados correctamente"))
            return redirect(reverse("speakers:edit"))
        return render(request, "speakers/edit.html", data)


class RestorePasswordView(View):

    @staticmethod
    def get(request, restore_code):
        try:
            reviewer = Speaker.objects.get(restore_code=restore_code)
        except Speaker.DoesNotExist:
            raise Http404
        data = {
            "reviewer": reviewer,
            "restore_code": restore_code,
            "form": RestorePasswordForm(initial={"restore_code": restore_code, "email": reviewer.user.email})
        }
        return render(request, "speakers/restore.html", data)

    @staticmethod
    def post(request, restore_code):
        form = RestorePasswordForm(request.POST)
        try:
            reviewer = Speaker.objects.get(restore_code=restore_code)
        except Speaker.DoesNotExist:
            raise Http404
        if form.is_valid():
            user = reviewer.user
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            reviewer.restore_code = None
            reviewer.save()
            messages.success(request, _("Se ha establecido la nueva contraseña"))
            return redirect(reverse("speakers:sign-in"))
        data = {
            "reviewer": reviewer,
            "restore_code": restore_code,
            "form": form
        }
        return render(request, "speakers/restore.html", data)


class RequestRestorePasswordView(View):

    @staticmethod
    def get(request):
        data = {
            "form": RequestRestoreCodeForm()
        }
        return render(request, "speakers/request_code.html", data)

    @staticmethod
    def post(request):
        form = RequestRestoreCodeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                review = Speaker.objects.get(user__email=email)
            except Speaker.DoesNotExist:
                messages.error(request, _("No se ha encontrado el correo electrónico."))
                return redirect("speakers:request_restore_password")
            review.send_restore_password_link()
            messages.success(request, _("Se ha enviado un correo a tu dirección "
                                        "con un enlace para establecer tu contraseña."))
        data = {
            "form": form
        }
        return render(request, "speakers/request_code.html", data)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from functools import update_wrapper

from django.contrib import admin
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from attendees.forms import ImportAttendeeForm, AdminAttendeeForm
from attendees.models import Attendee
from proposals.actions import export_as_csv_action


class AttendeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'email', 'dni', 'tracker']
    search_fields = ("name", "email", "tracker", "dni")
    actions = [export_as_csv_action("CSV Export", fields=[
        "id",
        "name",
        "email",
        "dni",
        "tracker",
        "notes",
        "allergies",
        "restore_code",
        "workshop_attendance"
    ])]
    form = AdminAttendeeForm

    def get_urls(self):
        """Override to add URL to import data."""
        from django.conf.urls import url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.model_name
        return [
            url(r"^import-data/$", wrap(self.import_data), name="%s_%s_import_data" % info),
        ] + super(AttendeeAdmin, self).get_urls()

    def import_data(self, request):
        """Admin view to import data from Ticketea."""
        opts = self.model._meta
        app_label = opts.app_label
        if not self.has_change_permission(request, None):
            raise PermissionDenied

        # Custom code for import data...
        if request.method == "POST":
            import_form = ImportAttendeeForm(request.POST, request.FILES)
            if import_form.is_valid():
                import_form.save()
                msg = _("Attendees imported!")
                self.message_user(request, msg, messages.SUCCESS)
        else:
            import_form = ImportAttendeeForm()

        # Common context for admin views
        context = dict(
            self.admin_site.each_context(request),
            title="Import data",
            module_name=force_text(opts.verbose_name_plural),
            import_form=import_form
        )
        request.current_app = self.admin_site.name
        return render(request, 'admin/%s/%s/import.html' % (app_label, opts.model_name), context)


admin.site.register(Attendee, AttendeeAdmin)

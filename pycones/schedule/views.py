# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from configurations.models import Option
from schedule.helpers import export_to_pentabarf, export_to_xcal, export_to_icalendar
from schedule.models import Schedule


def check_schedule_view(request):
    is_schedule_opened = bool(Option.objects.get_value("schedule_opened", 0))
    if not is_schedule_opened or not request.user.is_authenticated() or not request.user.is_superuser:
        raise Http404()


class ShowSchedule(View):
    """Shows the schedule of the event."""
    template_name = "schedule/show.html"

    def get(self, request):
        check_schedule_view(request)
        schedule = Schedule.objects.filter(published=True, hidden=False).first()
        data = {"days": []}
        for day in schedule.day_set.all():
            data["days"].append({
                "date": day.date,
                "slots": day.slot_set.all().select_related()
            })
        return render(request, self.template_name, data)


def pentabarf_view(request):
    """Download Pentabarf calendar file.
    :param request:
    """
    check_schedule_view(request)
    schedule = Schedule.objects.filter(published=True, hidden=False).first()
    pentabarf_xml = export_to_pentabarf(schedule)
    return HttpResponse(pentabarf_xml, content_type="application/xml")


def xcal_view(request):
    """Download xCal file.
    :param request:
    """
    check_schedule_view(request)
    schedule = Schedule.objects.filter(published=True, hidden=False).first()
    xcal_xml = export_to_xcal(schedule)
    return HttpResponse(xcal_xml, content_type="application/xml")


def icalendar_view(request):
    """Download iCalendar file.
    :param request:
    """
    check_schedule_view(request)
    schedule = Schedule.objects.filter(published=True, hidden=False).first()
    calendar_text = export_to_icalendar(schedule)
    return HttpResponse(calendar_text, content_type="text/calendar")
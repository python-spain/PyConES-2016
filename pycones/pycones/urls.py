# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from core.views import LogoutView
from schedule.views import icalendar_view

admin.autodiscover()

urlpatterns = i18n_patterns(
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^log-out/$', LogoutView.as_view(), name="log-out"),
    url(r'^tickets/$', TemplateView.as_view(template_name='pages/tickets.html'), name="tickets"),
    url(r'^code-of-conduct/$', TemplateView.as_view(template_name='pages/code_of_conduct.html'), name="code_of_conduct"),
    url(r'^keynoters-speakers/$', TemplateView.as_view(template_name='pages/keynoters.html'), name="keynoters"),
    url(r'^info/$', TemplateView.as_view(template_name='pages/info.html'), name="info"),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^proposals/', include('proposals.urls', namespace="proposals")),
    url(r'^reviewers/', include('reviewers.urls', namespace="reviewers")),
    # url(r'^schedule/', include('schedule.urls', namespace="schedule")),
    # url(r'^attendees/', include('attendees.urls', namespace="attendees")),
)

urlpatterns += [
    # url(r'schedule/pentabarf\.xml', pentabarf_view, name="schedule_pentabarf"),
    # url(r'schedule/xcal\.xml', xcal_view, name="schedule_xcal"),
    url(r'schedule\.ics', icalendar_view, name="schedule_icalendar"),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^rosetta/', include('rosetta.urls')),
    ]

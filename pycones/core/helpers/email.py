# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from smtplib import SMTPAuthenticationError
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template


def send_template_email(subject, from_email, to, template_name, context=Context()):
    """
    :param subject:
    :param from_email:
    :param to: list or string
    :param template_name:
    :param context:
    """
    current_site = Site.objects.get_current()
    context.update({
        "site": current_site,
        "static": "https://{}{}".format(
            current_site.domain,
            settings.STATIC_URL
        )
    })

    template = get_template(template_name)
    content = template.render(context)
    if not isinstance(to, list):
        to = [to]
    msg = EmailMultiAlternatives(subject, content, from_email, to)
    msg.attach_alternative(content, "text/html")
    try:
        msg.send()
    except SMTPAuthenticationError:
        pass

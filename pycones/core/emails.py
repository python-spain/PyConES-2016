# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import

import bleach
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email_multi_alternatives(subject, message_txt, message, from_email, to):
    """Sends an email using EmailMultiAlternatives"""
    email = EmailMultiAlternatives(subject=subject, body=message_txt, from_email=from_email, to=to)
    email.attach_alternative(message, "text/html")
    email.send()


def send_email(context, template, subject, from_email, to, content=None):
    """Sends an email using a template as content."""
    if not isinstance(to, list) and not isinstance(to, tuple):
        to = [to]
    if content is not None and 'content' not in context:
        context['content'] = content
    message = render_to_string(template, context)
    message_txt = message.replace("\n", "")
    message_txt = message_txt.replace("</p>", "\n")
    message_txt = message_txt.replace("</h1>", "\n\n")
    message_txt = bleach.clean(message_txt, strip=True)
    send_email_multi_alternatives(subject, message_txt, message, from_email, to)

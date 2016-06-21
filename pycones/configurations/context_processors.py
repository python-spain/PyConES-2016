# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import

from configurations.models import Option


def options(request):
    return {
        "is_submit_proposal_opened": bool(Option.objects.get_value("submit_proposal_opened", 1)),
        "is_activated_tickets_sale_button":  bool(Option.objects.get_value("activated_tickets_sale_button", 0)),
        "is_activated_tickets_sale_page":  bool(Option.objects.get_value("activated_tickets_sale_page", 0)),
        "sold_out": bool(Option.objects.get_value("sold_out", 0)),
    }

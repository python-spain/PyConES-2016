# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import

from configurations.models import Option


def submit_proposals(request):
    return {
        "is_submit_proposal_opened": bool(Option.objects.get_value("submit_proposal_opened", 1))
    }

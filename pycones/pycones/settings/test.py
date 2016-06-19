# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from .base import *

########## IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}
########## END IN-MEMORY TEST DATABASE

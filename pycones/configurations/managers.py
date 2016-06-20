# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six
from django.db import models


class OptionManager(models.Manager):
    """Manager for options."""

    def get_value(self, name, default=None):
        """Gets the value with the proper type."""
        converter = {
            self.model.INT: int,
            self.model.FLOAT: float,
            self.model.STRING: six.text_type
        }
        try:
            option = self.model.objects.get(name=name)
            if not option.is_list:
                return converter.get(option.type, six.text_type)(option.value)
            else:
                values = option.value.split(",")
                return list(map(lambda item: converter.get(option.type, six.text_type)(item), values))
        except self.model.DoesNotExist:
            return default

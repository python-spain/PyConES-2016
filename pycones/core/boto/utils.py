# -*- coding: utf-8 -*-
"""Storages for split media and static in different folders."""
from __future__ import unicode_literals
from pipeline.storage import PipelineMixin
import storages.backends.s3boto
 
 
class StaticRootS3BotoStorage(storages.backends.s3boto.S3BotoStorage):
    """Storage for save all static files in static folder."""
 
    def __init__(self, *args, **kwargs):
        """Overrides and define location in "static".
        
        @param args:
        @param kwargs:
        """
        kwargs['location'] = "static"
        super(StaticRootS3BotoStorage, self).__init__(*args, **kwargs)
 
 
class MediaRootS3BotoStorage(storages.backends.s3boto.S3BotoStorage):
    """Storage for save all media files in media folder."""
 
    def __init__(self, *args, **kwargs):
        """Overrides and define location in "media".
    
        @param args:
        @param kwargs:
        """
        kwargs['location'] = "media"
        super(MediaRootS3BotoStorage, self).__init__(*args, **kwargs)


class PipelineStaticRootS3BotoStorage(PipelineMixin, storages.backends.s3boto.S3BotoStorage):
    """Storage for save all static files in static folder."""

    def __init__(self, *args, **kwargs):
        """Overrides and define location in "static".

        @param args:
        @param kwargs:
        """
        kwargs['location'] = "static"
        super(PipelineStaticRootS3BotoStorage, self).__init__(*args, **kwargs)


class PipelineMediaRootS3BotoStorage(PipelineMixin, storages.backends.s3boto.S3BotoStorage):
    """Storage for save all media files in media folder."""

    def __init__(self, *args, **kwargs):
        """Overrides and define location in "media".

        @param args:
        @param kwargs:
        """
        kwargs['location'] = "media"
        super(PipelineMediaRootS3BotoStorage, self).__init__(*args, **kwargs)
"""Custom storage classes for static and media files."""
from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class StaticStorage(S3BotoStorage):
    """Static storage."""

    location = settings.STATICFILES_LOCATION


class MediaStorage(S3BotoStorage):
    """Media Storage."""

    location = settings.MEDIAFILES_LOCATION

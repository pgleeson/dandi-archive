from rest_framework import status

from dandiapi.api.services.exceptions import DandiError


class AssetHasBeenPublishedError(DandiError):
    http_status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = 'This asset has been published and cannot be modified.'


class VersionHasBeenPublishedError(DandiError):
    http_status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = 'This version has been published and cannot be modified.'

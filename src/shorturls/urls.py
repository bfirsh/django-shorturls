from django.conf import settings
from django.http import HttpResponse
from django.urls import re_path

from . import views


def handler404(request, exception=None):
    return HttpResponse(status=404)

urlpatterns = [
    re_path(
        r'^(?P<prefix>{prefix})(?P<tiny>\w+)$'.format(
            prefix='|'.join(settings.SHORTEN_MODELS.keys())),
        views.redirect,
    ),
]

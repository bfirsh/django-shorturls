from django.conf import settings
from django.urls import re_path
from django.http import HttpResponse

from . import views


def handler404(req):
    return HttpResponse(status=404)


urlpatterns = [
    re_path(
        r'^(?P<prefix>{0!s})(?P<tiny>\w+)$'.format(
            '|'.join(settings.SHORTEN_MODELS.keys())),
        views.redirect,
    ),
]

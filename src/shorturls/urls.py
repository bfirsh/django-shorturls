from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse

from . import views


def handler404(req):
    return HttpResponse(status=404)

urlpatterns = [
    url(
        regex=r'^(?P<prefix>{0!s})(?P<tiny>\w+)$'.format(
            '|'.join(settings.SHORTEN_MODELS.keys())),
        view=views.redirect,
    ),
]

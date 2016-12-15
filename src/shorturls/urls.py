from django.conf import settings
from django.conf.urls import *

urlpatterns = patterns('', 
    url(
        regex = '^(?P<prefix>{0!s})(?P<tiny>\w+)$'.format('|'.join(settings.SHORTEN_MODELS.keys())),
        view  = 'shorturls.views.redirect',
    ),
)

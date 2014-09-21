from django.conf import settings
from django.conf.urls import *

urlpatterns = patterns('', 
    url(
        regex = '^(?P<prefix>%s)(?P<tiny>\w+)$' % '|'.join(settings.SHORTEN_MODELS.keys()),
        view  = 'shorturls.views.redirect',
    ),
)

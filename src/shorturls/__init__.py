from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
try:
    from importlib import import_module
except:
    from django.utils.importlib import import_module
from shorturls import baseconv

default_converter = baseconv.base62

if hasattr(settings, 'SHORTURLS_DEFAULT_CONVERTER'):
    mod_name, conv_name = settings.SHORTURLS_DEFAULT_CONVERTER.rsplit('.', 1)
    try:
        mod = import_module(mod_name)
    except ImportError as e:
        raise ImproperlyConfigured(
            'Could not load converter specified by SHORTURLS_DEFAULT_CONVERTER. Error was: {0!s}'.format(e))
    try:
        default_converter = getattr(mod, conv_name)
    except AttributeError:
        raise ImproperlyConfigured(
            'Could not load converter specified by SHORTURLS_DEFAULT_CONVERTER. {0!s} is not in {1!s}.'.format(conv_name, mod))

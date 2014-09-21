# -*- coding: utf-8 -*-

# Code extracted from the project "django-shortim":
#  * https://github.com/valvim/django-shortim/
#  * https://github.com/valvim/django-shortim/blob/master/src/shortim/models.py
#
# Author: Arthur Furlan <afurlan@valv.im>

from django.db import models
from django.conf import settings
import string

## set the default shorturl chars
DEFAULT_SHORTURL_CHARS = string.uppercase
DEFAULT_SHORTURL_CHARS += string.lowercase
DEFAULT_SHORTURL_CHARS += string.digits

## allow user to configure a different chars chain
SHORTURL_CHARS = getattr(settings,
    'SHORTURL_CHARS', DEFAULT_SHORTURL_CHARS)

class SequenceMapper(object):

    @staticmethod
    def from_decimal(number):
        base = len(SHORTURL_CHARS)
        code = ''

        ## generate the respective code of the sequence
        index = 1
        while number > 0 and index+1 > 0:
            index = number % base - 1
            code = SHORTURL_CHARS[index] + code
            number = number / base
            if number > 0 and index < 0:
                number -= 1
                index = 0
        return code

    @staticmethod
    def to_decimal(code):
        base = len(SHORTURL_CHARS)
        number = 0

        ## calculate the respective number of the code
        for i, c in enumerate(code[::-1]):
            index = SHORTURL_CHARS.index(c)
            number += base ** i * (index+1)
        return number

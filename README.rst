django-shorturls
================

.. image:: https://travis-ci.org/bfirsh/django-shorturls.svg?branch=master
    :target: https://travis-ci.org/bfirsh/django-shorturls
.. image:: https://badge.fury.io/py/django-shorturls.svg
    :target: http://badge.fury.io/py/django-shorturls

A custom URL shortening app for Django, including easy ``rev=canonical``
support.

Most code was originally by Simon Willison; see
https://simonwillison.net/2009/Apr/11/revcanonical/ for details. Improved
slightly and packaged by Jacob Kaplan-Moss. Currently maintained by
Ben Firshman.

Patches welcome: http://github.com/bfirsh/django-shorturls

Usage
=====

So, you want to host your own short URLs on your Django site:

1. In your settings, define a set of prefixes for short URLs:

   .. code-block:: python
   
        SHORTEN_MODELS = {
            'A': 'myapp.animal',
            'V': 'myapp.vegetable',
            'M': 'myapp.mineral'
        }

   The keys are string prefixes; they can be any string, actually,
   but since we're going for short a single character is probably good.
   
   Values are the (hopefully-familiar) ``"<app-name>.<model-class>"`` used
   by Django to identify a model. Remember: ``app-name`` is the
   (case-sensitive) last bit of your app's name in ``INSTALLED_APPS``, and
   ``<model-class>`` is your model class's name, lowercased.
   
   Make sure your models have a ``get_absolute_url()`` method defined.
    
2. Wire up the redirect view by adding to your URLconf:

   .. code-block:: python
   
        ('^short/', include('shorturls.urls'))
        
3. If you'd like to quickly link to shortened URLs in your templates, stick
   ``"shorturls"`` in ``INSTALLED_APPS``, and then in your templates do:
   
   .. code-block:: html+django
   
        {% load shorturl %}
        <a href="{% shorturl object %}">...</a>
        
   (where ``object`` is a model instance).
  
   Alternatively:
  
   .. code-block:: html+django
   
        {% load shorturl %}
        {% revcanonical object %}
        
   This generates the whole ``<link rev="canonical" href="...">`` tag for
   you.
            
That's it.

If you'd like more control, keep reading.

Settings
========

Available settings are:

``SHORTEN_MODELS``
    You've seen this one.
    
``SHORT_BASE_URL``
    If defined, the ``shorturl`` and ``revcanonical`` template tags will
    prefix generated URLs with this value. Use this if you've got a shorter
    domain name you'd like to use for small URLs.
    
    For example, given ``SHORT_BASE_URL = 'http://exm.pl/'``, ``{% shorturl
    obj %}`` would return something like ``http://exm.pl/AbCd``.

``SHORTEN_FULL_BASE_URL``
    The domain to redirect to when redirecting away from the small URL.
    Again, you'll use this if your short URL base and your "real" site
    differ.
    
    If not defined, the redirect view will try to guess the proper domain by
    consulting the ``django.contrib.sites`` framework, if installed, or the
    requested domain, if not.


``SHORTURLS_DEFAULT_CONVERTER``
    The converter that is used to translate between short URLs and model IDs.
    Defaults to the built in base 62 conversion.

    Available converters:

    - ``shorturls.baseconv.base62`` Base 62 encoding.
    - ``shorturls.baseconv.base32`` `Douglas Crockford's base 32`_.
    - ``shorturls.baseconv.hexconv`` Hex encoding.
    - ``shorturls.baseconv.bin`` Binary encoding, because why not.

.. _Douglas Crockford's base 32: http://www.crockford.com/wrmg/base32.html

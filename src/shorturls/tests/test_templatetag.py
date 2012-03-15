from django.template import Template, Context
from django.conf import settings
from django.test import TestCase
from shorturls.tests.models import Animal, Vegetable, Mineral

class TemplateTagTestCase(TestCase):
    urls = 'shorturls.urls'
    fixtures = ['shorturls-test-data.json']

    def setUp(self):
        self.old_shorten = getattr(settings, 'SHORTEN_MODELS', None)
        self.old_base = getattr(settings, 'SHORT_BASE_URL', None)
        settings.SHORT_BASE_URL = None
        settings.SHORTEN_MODELS = {
            'A': 'shorturls.animal',
            'V': 'shorturls.vegetable',
        }

    def tearDown(self):
        if self.old_shorten is not None:
            settings.SHORTEN_MODELS = self.old_shorten
        if self.old_base is not None:
            settings.SHORT_BASE_URL = self.old_base

    def render(self, t, **c):
        return Template('{% load shorturl %}'+t).render(Context(c))

    def test_shorturl(self):
        r = self.render('{% shorturl a %}', a=Animal.objects.get(id=12345))
        self.assertEqual(r, '/ADNH')

    def test_bad_context(self):
        r = self.render('{% shorturl a %}')
        self.assertEqual(r, '')

    def test_no_prefix(self):
        r = self.render('{% shorturl m %}', m=Mineral.objects.all()[0])
        self.assertEqual(r, '')

    def test_short_base_url(self):
        settings.SHORT_BASE_URL = 'http://example.com/'
        r = self.render('{% shorturl a %}', a=Animal.objects.get(id=12345))
        self.assertEqual(r, 'http://example.com/ADNH')

    def test_revcanonical(self):
        r = self.render('{% revcanonical a %}', a=Animal.objects.get(id=12345))
        self.assertEqual(r, '<link rev="canonical" href="/ADNH">')

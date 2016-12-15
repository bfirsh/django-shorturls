from django.template import Template, Context
from django.conf import settings
from django.test import TestCase, override_settings
from shorturls.tests.models import Animal, Vegetable, Mineral


@override_settings(
    ROOT_URLCONF='shorturls.urls',
    SHORTEN_MODELS={
        'A': 'shorturls.animal',
        'V': 'shorturls.vegetable',
    },
)
class TemplateTagTestCase(TestCase):
    fixtures = ['shorturls-test-data.json']

    def setUp(self):
        settings.SHORT_BASE_URL = None

    def render(self, t, **c):
        return Template('{% load shorturl %}' + t).render(Context(c))

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

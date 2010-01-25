from django.conf import settings
from django.test import TestCase
from shorturls.baseconv import base62

class RedirectViewTestCase(TestCase):
    urls = 'shorturls.urls'
    fixtures = ['shorturls-test-data.json']
    
    def setUp(self):
        self.old_shorten = getattr(settings, 'SHORTEN_MODELS', None)
        self.old_base = getattr(settings, 'SHORTEN_FULL_BASE_URL', None)
        settings.SHORTEN_MODELS = {
            'A': 'shorturls.animal',
            'V': 'shorturls.vegetable',
            'M': 'shorturls.mineral',
            'bad': 'not.amodel',
            'bad2': 'not.even.valid',
        }
        settings.SHORTEN_FULL_BASE_URL = 'http://example.com'
        
    def tearDown(self):
        if self.old_shorten is not None:
            settings.SHORTEN_MODELS = self.old_shorten
        if self.old_base is not None:
            settings.SHORTEN_FULL_BASE_URL = self.old_base
    
    def test_redirect(self):
        """
        Test the basic operation of a working redirect.
        """
        response = self.client.get('/A%s' % enc(12345))
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['Location'], 'http://example.com/animal/12345/')
        
    def test_redirect_from_request(self):
        """
        Test a relative redirect when the Sites app isn't installed.
        """
        settings.SHORTEN_FULL_BASE_URL = None
        response = self.client.get('/A%s' % enc(54321), HTTP_HOST='example.org')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['Location'], 'http://example.org/animal/54321/')
        
    def test_redirect_complete_url(self):
        """
        Test a redirect when the object returns a complete URL.
        """
        response = self.client.get('/V%s' % enc(785))
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['Location'], 'http://example.net/veggies/785')
        
    def test_bad_short_urls(self):
        self.assertEqual(404, self.client.get('/badabcd').status_code)
        self.assertEqual(404, self.client.get('/bad2abcd').status_code)
        self.assertEqual(404, self.client.get('/Vssssss').status_code)

    def test_model_without_get_absolute_url(self):
        self.assertEqual(404, self.client.get('/M%s' % enc(10101)).status_code)
        
def enc(id):
    return base62.from_decimal(id)

import urlparse
from django import template
from django.conf import settings
from django.core import urlresolvers
from django.utils.safestring import mark_safe
from shorturls import default_converter as converter

class ShortURL(template.Node):
    @classmethod
    def parse(cls, parser, token):
        parts = token.split_contents()
        if len(parts) != 2:
            raise template.TemplateSyntaxError("%s takes exactly one argument" % parts[0])
        return cls(template.Variable(parts[1]))
        
    def __init__(self, obj):
        self.obj = obj
        
    def render(self, context):
        try:
            obj = self.obj.resolve(context)
        except template.VariableDoesNotExist:
            return ''
            
        try:
            prefix = self.get_prefix(obj)
        except (AttributeError, KeyError):
            return ''
        
        tinyid = converter.from_decimal(obj.pk)
                
        if hasattr(settings, 'SHORT_BASE_URL') and settings.SHORT_BASE_URL:
            return urlparse.urljoin(settings.SHORT_BASE_URL, prefix+tinyid)
        
        try:
            return urlresolvers.reverse('shorturls.views.redirect', kwargs = {
                'prefix': prefix,
                'tiny': tinyid
            })
        except urlresolvers.NoReverseMatch:
            return ''
            
    def get_prefix(self, model):
        if not hasattr(self.__class__, '_prefixmap'):
            self.__class__._prefixmap = dict((m,p) for p,m in settings.SHORTEN_MODELS.items())
        key = '%s.%s' % (model._meta.app_label, model.__class__.__name__.lower())
        return self.__class__._prefixmap[key]
        
class RevCanonical(ShortURL):
    def render(self, context):
        url = super(RevCanonical, self).render(context)
        if url:
            return mark_safe('<link rev="canonical" href="%s">' % url)
        else:
            return ''

register = template.Library()
register.tag('shorturl', ShortURL.parse)
register.tag('revcanonical', RevCanonical.parse)
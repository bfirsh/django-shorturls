"""
Convert numbers from base 10 integers to base X strings and back again.

Original: http://www.djangosnippets.org/snippets/1431/

Sample usage:

>>> base20 = BaseConverter('0123456789abcdefghij')
>>> base20.from_decimal(1234)
'31e'
>>> base20.to_decimal('31e')
1234
"""

class BaseConverter(object):
    decode_mapping = {}
    
    def __init__(self, digits):
        self.digits = digits
        self.length = len(digits)
    
    def from_decimal(self, i):
        if i < 0:
            i, neg = -i, 1
        else:
            neg = 0
        enc = ''
        while i >= self.length:
            i, mod = divmod(i, self.length)
            enc = self.digits[mod] + enc
        enc = self.digits[i] + enc
        if neg:
            enc = '-' + enc
        return enc
    
    def to_decimal(self, s):
        if self.decode_mapping:
            new = ''
            for digit in s:
                if digit in self.decode_mapping:
                    new += self.decode_mapping[digit]
                else:
                    new += digit
            s = new
        if str(s)[0] == '-':
            s, neg = str(s)[1:], 1
        else:
            neg = 0
        decoded = 0
        multi = 1
        while len(s) > 0:
            decoded += multi * self.digits.index(s[-1:])
            multi = multi * self.length
            s = s[:-1]
        if neg:
            decoded = -decoded
        return decoded
    
bin = BaseConverter('01')
hexconv = BaseConverter('0123456789ABCDEF')
base62 = BaseConverter(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
)

class Base32Converter(BaseConverter):
    """
    http://www.crockford.com/wrmg/base32.html
    """
    decode_mapping = {
        'o': '0',
        'i': '1',
        'l': '1',
    }
    
    def __init__(self):
        super(Base32Converter, self).__init__('0123456789abcdefghjkmnpqrstvwxyz')
    
    def to_decimal(self, s):
        return super(Base32Converter, self).to_decimal(s.lower())

base32 = Base32Converter()

if __name__ == '__main__':
    import doctest
    doctest.testmod()


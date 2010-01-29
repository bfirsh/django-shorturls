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
    decimal_digits = "0123456789"
    decode_mapping = {}
    
    def __init__(self, digits):
        self.digits = digits
    
    def from_decimal(self, i):
        return self.convert(i, self.decimal_digits, self.digits)
    
    def to_decimal(self, s):
        if self.decode_mapping:
            new = ''
            for digit in s:
                if digit in self.decode_mapping:
                    new += self.decode_mapping[digit]
                else:
                    new += digit
            s = new
        return int(self.convert(s, self.digits, self.decimal_digits))
    
    def convert(number, fromdigits, todigits):
        # Based on http://code.activestate.com/recipes/111286/
        if str(number)[0] == '-':
            number = str(number)[1:]
            neg = 1
        else:
            neg = 0

        # make an integer out of the number
        x = 0
        for digit in str(number):
           x = x * len(fromdigits) + fromdigits.index(digit)
    
        # create the result in base 'len(todigits)'
        if x == 0:
            res = todigits[0]
        else:
            res = ""
            while x > 0:
                digit = x % len(todigits)
                res = todigits[digit] + res
                x = int(x / len(todigits))
            if neg:
                res = '-' + res
        return res
    convert = staticmethod(convert)

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


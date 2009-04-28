import unittest
from shorturls import baseconv

class BaseConvTests(unittest.TestCase):
    
    def _test_converter(self, converter):
        nums = [-10 ** 10, 10 ** 10] + range(-100, 100)
        for before in nums:
            after = converter.to_decimal(converter.from_decimal(before))
            self.assertEqual(before, after)
            
    def test_bin(self):
        self._test_converter(baseconv.bin)
        
    def test_hex(self):
        self._test_converter(baseconv.hexconv)
        
    def test_base62(self):
        self._test_converter(baseconv.base62)
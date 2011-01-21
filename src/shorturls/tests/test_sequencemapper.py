import unittest
from shorturls.sequencemapper import SequenceMapper

class SequenceMapperTests(unittest.TestCase):
    
    def test_mapper(self):
        nums = [-10 ** 10, 10 ** 10] + range(-100, 100)
        for before in nums:
            after = SequenceMapper.to_decimal(converter.from_decimal(before))
            self.assertEqual(before, after)

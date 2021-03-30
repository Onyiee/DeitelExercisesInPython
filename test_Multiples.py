from unittest import TestCase
from Multiples import is_multiple


class Multiples_Test(TestCase):
    def test_is_multiple(self):
        self.assertTrue(is_multiple(2, 4))
        self.assertFalse(is_multiple(9, 2))

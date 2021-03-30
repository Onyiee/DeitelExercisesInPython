from unittest import TestCase
from odd_or_even import is_even


class Test_odd_or_even(TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(9))
        self.assertFalse(is_even(-1))

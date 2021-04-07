from unittest import TestCase
from Perfect_number import perfect_numbers


class Test_Perfect_number(TestCase):
    def test_perfect_numbers(self):
        self.assertTrue(perfect_numbers(6))

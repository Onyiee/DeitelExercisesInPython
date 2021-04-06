from unittest import TestCase
from Prime_numbers import prime_numbers


class Test_prime_numbers(TestCase):
    def test_prime_numbers(self):

        self.assertTrue(prime_numbers(11))

        self.assertFalse( prime_numbers(12))

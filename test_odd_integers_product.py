from unittest import TestCase
from odd_integers_product import odd_integers_product


class Test_odd_integers_product(TestCase):
    def test_odd_integers_product(self):
        self.assertEqual(2027025, odd_integers_product())

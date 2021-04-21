from unittest import TestCase
from variable_length_args import product


class Test_variable_length_args(TestCase):
    def test_product(self):
        self.assertEqual(4, product(2, 2))
        self.assertEqual(60480, product(2, 5, 2, 6, 7, 8, 9))
        self.assertEqual(17418240, product(3, 8, 3, 9, 2, 4, 8, 6, 70))

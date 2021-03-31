from unittest import TestCase
from minimum_number import minimum3


class Test_minimum_number(TestCase):
    def test_minimum3(self):
        minimum3(3, 8, 1)
        self.assertEqual(1, minimum3(3, 8, 1))

from unittest import TestCase
from minimum_number import minimum3


class Test_minimum_number(TestCase):
    def test_minimum3(self):
        list_of_numbers = [9, 1, 2, 3, 4, 5]
        minimum3(list_of_numbers)
        self.assertEqual(1, minimum3(list_of_numbers))
        self.assertNotEqual(2, minimum3(list_of_numbers))

from unittest import TestCase
from circle_area import circle_area


class Test_circle_area(TestCase):
    def test_circle_area(self):
        self.assertEqual(78.55, circle_area(5))
        self.assertEqual(28.278, circle_area(3))

from unittest import TestCase

from Coin_Tossing import coin_tossing


class Test_Coin_Tossing(TestCase):
    def test_coin_tossing(self):
        self.assertIsNotNone(coin_tossing())

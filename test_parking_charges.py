from unittest import TestCase

from parking_charges import Car_park_charges_calculator


class Car_park_charges_calculator_Test(TestCase):
    def setUp(self) -> None:
        self.car_park_charges_calculator = Car_park_charges_calculator()

    def tearDown(self) -> None:
        self.car_park_charges_calculator = None

    def test_set_hours_parked(self):
        self.car_park_charges_calculator.set_hours_parked(5)
        self.assertEqual(5, self.car_park_charges_calculator.get_hours_parked())

    def test_set_fee(self):
        self.car_park_charges_calculator.set_fee_for_hours_parked(0.50)
        self.assertEqual(0.50, self.car_park_charges_calculator.get_fee_for_hours_parked())

    def test_charges_can_be_calculated(self):
        self.car_park_charges_calculator.get_hours_parked()
        self.car_park_charges_calculator.get_fee_for_hours_parked()
        self.car_park_charges_calculator.calculate_charges(3)
        self.assertEqual(2.00, self.car_park_charges_calculator.get_charges())
        self.car_park_charges_calculator.calculate_charges(24)
        self.assertEqual(10.00, self.car_park_charges_calculator.get_charges())
        self.car_park_charges_calculator.calculate_charges(14)
        self.assertEqual(7.5, self.car_park_charges_calculator.get_charges())




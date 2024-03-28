from unittest import TestCase, main
from car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Audi", "A6", 10, 100)

    def test_correct_init_(self):
        self.assertEqual("Audi", self.car.make)
        self.assertEqual("A6", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_incorrect_input_for_make(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_incorrect_input_for_model(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_incorrect_input_for_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_incorrect_input_for_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_incorrect_input_for_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -7

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_or_negative_amount_(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_less_than_max_capacity(self):
        self.car.refuel(10)
        expected_fuel_amount = 10
        self.assertEqual(expected_fuel_amount, self.car.fuel_amount)

    def test_refuel_with_more_than_max_capacity(self):
        self.car.refuel(150)
        expected_fuel_amount = 100
        self.assertEqual(expected_fuel_amount, self.car.fuel_amount)

    def test_successful_drive(self):
        self.car.fuel_amount = 20
        self.car.drive(100)
        self.assertEqual(10, self.car.fuel_amount)

    def test_not_enough_fuel_amount_for_a_drive(self):
        self.car.fuel_amount = 10

        with self.assertRaises(Exception) as ex:
            self.car.drive(200)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()

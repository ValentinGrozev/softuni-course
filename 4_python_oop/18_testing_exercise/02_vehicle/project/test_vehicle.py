from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(100, 200)

    def test_correct__init__(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_insufficient_fuel_amount(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_success_drive(self):
        self.vehicle.drive(50)
        self.assertEqual(37.50, self.vehicle.fuel)

    def test_success_refuel(self):
        self.vehicle.fuel = 10
        self.vehicle.refuel(50)
        self.assertEqual(60, self.vehicle.fuel)

    def test_fail_if_fuel_exceed_limit(self):
        self.vehicle.fuel = 60

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(50)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_vehicle_information(self):
        expected_result = "The vehicle has 200 horse power with 100 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, self.vehicle.__str__())


if __name__ == '__main__':
    main()

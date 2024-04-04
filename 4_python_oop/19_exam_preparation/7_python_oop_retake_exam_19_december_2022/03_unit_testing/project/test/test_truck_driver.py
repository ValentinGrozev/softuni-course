from unittest import TestCase, main

from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self):
        self.td = TruckDriver("Andy", 100)

    def test__init__(self):
        self.assertEqual("Andy", self.td.name)
        self.assertEqual(100, self.td.money_per_mile)
        self.assertEqual({}, self.td.available_cargos)
        self.assertEqual(0, self.td.earned_money)
        self.assertEqual(0, self.td.miles)

    def test_negative_earned_money(self):
        with self.assertRaises(ValueError) as ve:
            self.td.earned_money = -10

        self.assertEqual(f"{self.td.name} went bankrupt.", str(ve.exception))

    def test_cant_add_cargo_because_location_is_already_done(self):
        self.td.available_cargos = {"Sofia": 3}
        with self.assertRaises(Exception) as ex:
            self.td.add_cargo_offer("Sofia", 3)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer(self):
        result = self.td.add_cargo_offer("Sofia", 3)
        expected_result = f"Cargo for 3 to Sofia was added as an offer."
        self.assertEqual(expected_result, result)

    def test_drive_without_offers(self):
        result = self.td.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_with_best_cargo_offer_without_activities(self):
        self.td.add_cargo_offer("Sofia", 3)
        self.td.add_cargo_offer("Manchester", 5)

        result = self.td.drive_best_cargo_offer()
        expected_result = f"{self.td.name} is driving 5 to Manchester."

        self.assertEqual(500, self.td.earned_money)
        self.assertEqual(5, self.td.miles)
        self.assertEqual(2, len(self.td.available_cargos))
        self.assertEqual(expected_result, result)

    def test_drive_250_miles(self):
        self.td.add_cargo_offer("Manchester", 250)
        self.td.drive_best_cargo_offer()
        self.assertEqual(24980, self.td.earned_money)
        self.assertEqual(250, self.td.miles)
        self.assertEqual(1, len(self.td.available_cargos))

    def test_drive_500_miles(self):
        self.td.add_cargo_offer("Manchester", 500)
        self.td.drive_best_cargo_offer()
        self.assertEqual(49960, self.td.earned_money)
        self.assertEqual(500, self.td.miles)
        self.assertEqual(1, len(self.td.available_cargos))

    def test_drive_1000_miles(self):
        self.td.money_per_mile = 5
        self.td.add_cargo_offer("Manchester", 1000)
        self.td.drive_best_cargo_offer()
        self.assertEqual(4875, self.td.earned_money)
        self.assertEqual(1000, self.td.miles)
        self.assertEqual(1, len(self.td.available_cargos))

    def test_drive_1500_miles(self):
        self.td.money_per_mile = 5
        self.td.add_cargo_offer("Manchester", 1500)
        self.td.drive_best_cargo_offer()
        self.assertEqual(6835, self.td.earned_money)
        self.assertEqual(1500, self.td.miles)
        self.assertEqual(1, len(self.td.available_cargos))

    def test_drive_10000_miles(self):
        self.td.money_per_mile = 5
        self.td.add_cargo_offer("Manchester", 10000)
        self.td.drive_best_cargo_offer()
        self.assertEqual(38250, self.td.earned_money)
        self.assertEqual(10000, self.td.miles)
        self.assertEqual(1, len(self.td.available_cargos))

    def test_repr_(self):
        self.td.add_cargo_offer("Manchester", 10000)
        self.td.drive_best_cargo_offer()
        expected_result = f"{self.td.name} has {self.td.miles} miles behind his back."
        self.assertEqual(repr(self.td), expected_result)


if __name__ == "__main__":
    main()

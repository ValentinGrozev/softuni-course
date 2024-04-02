from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):

    def setUp(self):
        self.trip = Trip(500.50, 2, True)

    def test__init__(self):
        self.assertEqual(500.50, self.trip.budget)
        self.assertEqual(2, self.trip.travelers)
        self.assertEqual(True, self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_are_travellers_more_than_one(self):
        self.assertEqual(2, self.trip.travelers)

    def test_to_make_a_trip_without_travellers(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual("At least one traveler is required!", str(ve.exception))

    def test_is_family_set_to_false(self):
        self.trip.travelers = 1
        self.trip.is_family = True

        self.assertFalse(self.trip.is_family)

    def test_is_family_set_to_true(self):
        self.trip.travelers = 4
        self.trip.is_family = True

        self.assertTrue(self.trip.is_family)

    def test_try_to_book_a_trip_to_destination_out_of_dictionary(self):
        result = self.trip.book_a_trip("England")
        expected_result = "This destination is not in our offers, please choose a new one!"
        self.assertEqual(expected_result, result)

    def test_budget_for_trip_is_not_enough_with_is_family_true(self):
        result = self.trip.book_a_trip("Australia")
        expected_result = "Your budget is not enough!"
        self.assertEqual(expected_result, result)

    def test_budget_for_trip_is_not_enough_with_is_family_False(self):
        self.trip.is_family = False
        result = self.trip.book_a_trip("Australia")
        expected_result = "Your budget is not enough!"
        self.assertEqual(expected_result, result)

    def test_budget_for_trip_is_enough_and_is_family_is_true(self):
        self.trip.budget = 100000
        result = self.trip.book_a_trip("Australia")
        expected_result = f'Successfully booked destination Australia! Your budget left is {self.trip.budget:.2f}'
        self.assertEqual(expected_result, result)
        self.assertEqual(89740, self.trip.budget)
        self.assertEqual(1, len(self.trip.booked_destinations_paid_amounts))

    def test_budget_for_trip_is_enough_and_is_family_is_false(self):
        self.trip.budget = 100000
        self.trip.is_family = False
        result = self.trip.book_a_trip("Australia")
        expected_result = f'Successfully booked destination Australia! Your budget left is {self.trip.budget:.2f}'
        self.assertEqual(expected_result, result)
        self.assertEqual(88600, self.trip.budget)
        self.assertEqual(1, len(self.trip.booked_destinations_paid_amounts))

    def test_no_bookings_in_booked_destinations(self):
        result = self.trip.booking_status()
        self.assertEqual(0, len(self.trip.booked_destinations_paid_amounts))
        self.assertEqual(f"No bookings yet. Budget: {self.trip.budget:.2f}", result)

    def test_bookings_in_booked_destinations(self):
        self.trip.budget = 100000
        self.trip.is_family = False
        self.trip.book_a_trip("Australia")
        self.trip.book_a_trip("Brazil")
        result = self.trip.booking_status()
        expected_result = "Booked Destination: Australia\n"
        expected_result += "Paid Amount: 11400.00\n"
        expected_result += "Booked Destination: Brazil\n"
        expected_result += "Paid Amount: 12400.00\n"
        expected_result += "Number of Travelers: 2\n"
        expected_result += "Budget Left: 76200.00"

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()

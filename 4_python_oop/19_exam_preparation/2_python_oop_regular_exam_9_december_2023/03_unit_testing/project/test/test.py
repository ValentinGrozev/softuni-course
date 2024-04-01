from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.rs = RailwayStation("Sofia")

    def test__init__(self):
        self.assertEqual("Sofia", self.rs.name)
        self.assertEqual(deque(), self.rs.arrival_trains)
        self.assertEqual(deque(), self.rs.departure_trains)

    def test_incorrect_name(self):
        with self.assertRaises(ValueError) as ve:
            self.rs.name = "Sl"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board_with_one_parameter(self):
        self.rs.new_arrival_on_board("Arrived")
        result = self.rs.arrival_trains

        expected_result = deque(["Arrived"])
        self.assertEqual(expected_result, result)

    def test_new_arrival_on_board_with_two_parameter(self):
        self.rs.new_arrival_on_board("Arrived")
        self.rs.new_arrival_on_board("Second")
        result = self.rs.arrival_trains

        expected_result = deque(["Arrived", "Second"])
        self.assertEqual(expected_result, result)

    def test_train_has_arrived_with_other_trains_info(self):
        self.rs.new_arrival_on_board("Arrived")
        result = self.rs.train_has_arrived("Second")

        self.assertEqual("There are other trains to arrive before Second.", result)

    def test_train_has_arrived_with_departure_info(self):
        self.rs.new_arrival_on_board("Arrived")
        result = self.rs.train_has_arrived("Arrived")

        self.assertEqual("Arrived is on the platform and will leave in 5 minutes.", result)
        self.assertEqual(1, len(self.rs.departure_trains))

    def test_train_has_left_with_correct_train_info(self):
        self.rs.new_arrival_on_board("Arrived")
        self.rs.train_has_arrived("Arrived")
        result = self.rs.train_has_left("Arrived")

        self.assertTrue(result)

    def test_train_has_left_with_incorrect_train_info(self):
        self.rs.new_arrival_on_board("Arrived")
        self.rs.train_has_arrived("Arrived")
        result = self.rs.train_has_left("Second")

        self.assertFalse(result)


if __name__ == "__main__":
    main()

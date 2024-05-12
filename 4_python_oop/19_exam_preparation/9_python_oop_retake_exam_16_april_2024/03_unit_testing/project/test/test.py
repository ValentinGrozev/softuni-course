from unittest import TestCase
from project.restaurant import Restaurant


class TestRestaurant(TestCase):
    def setUp(self):
        self.r = Restaurant("Manchester", 30)

    def test_init_(self):
        self.assertEqual(self.r.name, "Manchester")
        self.assertEqual(self.r.capacity, 30)
        self.assertEqual(self.r.waiters, [])

    def test_without_name(self):
        with self.assertRaises(ValueError) as ve:
            self.r = Restaurant("", 30)

        self.assertEqual("Invalid name!", str(ve.exception))

    def test_name_with_empty_spaces(self):
        with self.assertRaises(ValueError) as ve:
            self.r = Restaurant("       ", 30)

        self.assertEqual("Invalid name!", str(ve.exception))

    def test_with_negative_capacity(self):
        with self.assertRaises(ValueError) as ve:
            self.r = Restaurant("Manchester", -30)

        self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_get_waiters_expect_waiter(self):
        self.r.add_waiter("Ivan")
        result = self.r.get_waiters()
        expected_result = [{'name': 'Ivan'}]
        self.assertEqual(result, expected_result)

    def test_get_waiters_expect_waiter_min_earrings(self):
        self.r.add_waiter("Ivan")
        self.r.add_waiter("Nikolay")
        self.r.waiters[0]["total_earnings"] = 13
        self.r.waiters[1]["total_earnings"] = 350
        expected_result = [{"name": "Nikolay", "total_earnings": 350}]
        result = self.r.get_waiters(min_earnings=150)
        self.assertEqual(expected_result, result)

    def test_get_waiters_expect_waiter_max_earrings(self):
        self.r.add_waiter("Ivan")
        self.r.add_waiter("Nikolay")
        self.r.waiters[0]["total_earnings"] = 13
        self.r.waiters[1]["total_earnings"] = 350
        expected_result = [{"name": "Ivan", "total_earnings": 13}]
        result = self.r.get_waiters(max_earnings=150)
        self.assertEqual(expected_result, result)

    def test_get_waiters_expect_waiter_min_max_earrings(self):
        self.r.add_waiter("Ivan")
        self.r.add_waiter("Nikolay")
        self.r.add_waiter("Georgi")
        self.r.waiters[0]["total_earnings"] = 13
        self.r.waiters[1]["total_earnings"] = 350
        self.r.waiters[2]["total_earnings"] = 700
        expected_result = [{"name": "Georgi", "total_earnings": 700}]
        result = self.r.get_waiters(min_earnings=360, max_earnings=1500)
        self.assertEqual(expected_result, result)

    def test_add_waiter_successfully(self):
        result = self.r.add_waiter("Ivan")
        expected_result = "The waiter Ivan has been added."
        self.assertEqual(result, expected_result)

    def test_cant_add_waiter_because_of_capacity(self):
        self.r = Restaurant("Manchester", 1)
        self.r.add_waiter("Ivan")
        result = self.r.add_waiter("Anton")
        expected_result = "No more places!"
        self.assertEqual(result, expected_result)

    def test_cant_add_waiter_more_than_one_time(self):
        self.r = Restaurant("Manchester", 2)
        self.r.add_waiter("Ivan")
        result = self.r.add_waiter("Ivan")
        expected_result = "The waiter Ivan already exists!"
        self.assertEqual(result, expected_result)

    def test_remove_waiter(self):
        self.r.add_waiter("Ivan")
        result = self.r.remove_waiter("Ivan")
        expected_result = "The waiter Ivan has been removed."
        self.assertEqual(result, expected_result)

    def test_cant_remove_waiter_because_there_is_not_such_waiter(self):
        self.r.add_waiter("Ivan")
        result = self.r.remove_waiter("Nikolay")
        expected_result = "No waiter found with the name Nikolay."
        self.assertEqual(result, expected_result)

    def test_get_total_earnings_expect_zero_waiters(self):
        expected_result = 0
        result = self.r.get_total_earnings()
        self.assertEqual(result, expected_result)

    def test_get_total_earning_expect_one_waiter(self):
        self.r.add_waiter("Ivan")
        self.r.waiters[0]["total_earnings"] = 10
        expected_result = 10
        result = self.r.get_total_earnings()
        self.assertEqual(expected_result, result)

    def test_get_total_earning_expect_two_waiters(self):
        self.r.add_waiter("Ivan")
        self.r.waiters[0]["total_earnings"] = 10
        self.r.add_waiter("Georgi")
        self.r.waiters[1]["total_earnings"] = 40
        expected_result = 50
        result = self.r.get_total_earnings()
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()

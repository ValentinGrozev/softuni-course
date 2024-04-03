from unittest import TestCase, main

from project.robot import Robot


class TestRobot(TestCase):

    def setUp(self):
        self.robot = Robot(
            "123",
            "Education",
            5,
            1000)

    def test__init__(self):
        self.assertEqual("123", self.robot.robot_id)
        self.assertEqual("Education", self.robot.category)
        self.assertEqual(5, self.robot.available_capacity)
        self.assertEqual(1000, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_with_incorrect_category(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Sport"

        expected_result = f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'"
        self.assertEqual(expected_result, str(ve.exception))

    def test_with_correct_category(self):
        self.robot.category = "Education"
        self.assertEqual("Education", self.robot.category)

    def test_with_incorrect_price(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -200

        expected_result = "Price cannot be negative!"
        self.assertEqual(expected_result, str(ve.exception))

    def test_with_correct_price(self):
        self.robot.price = 1000
        self.assertEqual(1000, self.robot.price)

    def test_upgrade_robot_successful(self):
        result = self.robot.upgrade("Addition ram", 200)
        expected_result = f'Robot {self.robot.robot_id} was upgraded with Addition ram.'

        self.assertEqual(1, len(self.robot.hardware_upgrades))
        self.assertEqual(1300, self.robot.price)
        self.assertEqual(expected_result, result)

    def test_upgrade_robot_with_same_hardware_expect_error(self):
        self.robot.upgrade("Addition ram", 200)
        result = self.robot.upgrade("Addition ram", 200)
        expected_result = f"Robot {self.robot.robot_id} was not upgraded."

        self.assertEqual(expected_result, result)
        self.assertEqual(1, len(self.robot.hardware_upgrades))

    def test_update_robot_software_successful(self):
        result = self.robot.update(2.3, 2)
        expected_result = f'Robot {self.robot.robot_id} was updated to version 2.3.'

        self.assertEqual(expected_result, result)
        self.assertEqual(1, len(self.robot.software_updates))

    def test_to_update_robot_but_dont_have_enough_capacity(self):
        self.robot.update(1.3, 3)
        result = self.robot.update(2.3, 10)
        expected_result = f"Robot {self.robot.robot_id} was not updated."

        self.assertEqual(expected_result, result)
        self.assertEqual(1, len(self.robot.software_updates))

    def test_to_update_robot_but_version_is_lower_than_existing_one(self):
        self.robot.update(2.3, 2)
        result = self.robot.update(2.0, 2)
        expected_result = f"Robot {self.robot.robot_id} was not updated."

        self.assertEqual(expected_result, result)
        self.assertEqual(1, len(self.robot.software_updates))

    def test_compare_prices_between_two_robots_and_first_is_cheaper(self):
        robot_two = Robot(
            "345",
            "Education",
            5,
            2000)

        result = self.robot.__gt__(robot_two)
        expected_result = f'Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {robot_two.robot_id}.'
        self.assertEqual(result, expected_result)

    def test_compare_prices_between_two_robots_and_first_is_expensive(self):
        robot_two = Robot(
            "345",
            "Education",
            5,
            200)

        result = self.robot.__gt__(robot_two)
        expected_result = (f'Robot with ID {self.robot.robot_id} is more expensive than '
                           f'Robot with ID {robot_two.robot_id}.')
        self.assertEqual(result, expected_result)

    def test_compare_prices_between_two_robots_and_prices_are_equal(self):
        robot_two = Robot(
            "345",
            "Education",
            5,
            1000)

        result = self.robot.__gt__(robot_two)
        expected_result = f'Robot with ID {self.robot.robot_id} costs equal to Robot with ID {robot_two.robot_id}.'
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()

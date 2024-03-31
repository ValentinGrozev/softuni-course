from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):

    def setUp(self):
        self.robot = ClimbingRobot(
            "Alpine",
            "Ram",
            50,
            100)

    def test__init__(self):
        self.assertEqual("Alpine", self.robot.category)
        self.assertEqual("Ram", self.robot.part_type)
        self.assertEqual(50, self.robot.capacity)
        self.assertEqual(100, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test__incorrect_category(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Street"

        expected_result = f"Category should be one of {self.robot.ALLOWED_CATEGORIES}"
        self.assertEqual(expected_result, str(ve.exception))

    def test_get_used_capacity(self):
        self.robot.installed_software = [
            {"name": "Word", "capacity_consumption": 20, "memory_consumption": 30},
            {"name": "Excell", "capacity_consumption": 10, "memory_consumption": 40}
        ]
        self.assertEqual(30, self.robot.get_used_capacity())

    def test_get_available_capacity(self):
        self.robot.installed_software = [
            {"name": "Word", "capacity_consumption": 20, "memory_consumption": 30},
            {"name": "Excell", "capacity_consumption": 10, "memory_consumption": 40}
        ]
        self.assertEqual(self.robot.capacity - self.robot.get_used_capacity(), self.robot.get_available_capacity())

    def test_get_used_memory(self):
        self.robot.installed_software = [
            {"name": "Word", "capacity_consumption": 20, "memory_consumption": 30},
            {"name": "Excell", "capacity_consumption": 10, "memory_consumption": 40}
        ]
        self.assertEqual(70, self.robot.get_used_memory())

    def test_get_available_memory(self):
        self.robot.installed_software = [
            {"name": "Word", "capacity_consumption": 20, "memory_consumption": 30},
            {"name": "Excell", "capacity_consumption": 10, "memory_consumption": 40}
        ]
        self.assertEqual(self.robot.memory - self.robot.get_used_memory(), self.robot.get_available_memory())

    def test_install_software_with_max_values_for_capacity_and_memory(self):
        result = self.robot.install_software(
            {"name": "Word", "capacity_consumption": 50, "memory_consumption": 100})

        expected_result = f"Software 'Word' successfully installed on {self.robot.category} part."

        self.assertEqual(expected_result, result)

    def test_install_software_with_more_capacity_than_what_we_have(self):
        result = self.robot.install_software(
            {"name": "Word", "capacity_consumption": 150, "memory_consumption": 100})

        expected_result = f"Software 'Word' cannot be installed on {self.robot.category} part."

        self.assertEqual(expected_result, result)

    def test_install_software_with_more_memory_than_what_we_have(self):
        result = self.robot.install_software(
            {"name": "Word", "capacity_consumption": 30, "memory_consumption": 150})

        expected_result = f"Software 'Word' cannot be installed on {self.robot.category} part."

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()

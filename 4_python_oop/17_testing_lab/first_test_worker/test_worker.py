from unittest import TestCase, main
from worker import Worker


class TestWorker(TestCase):

    def setUp(self):
        self.worker = Worker("Ivan", 100, 50)

    def test_correct__init__(self):
        self.assertEqual("Ivan", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(50, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_try_to_work_with_no_energy_expect_raise_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_try_to_work_with_enough_energy_expect_to_increase_salary_and_decrease_energy(self):
        expected_money = self.worker.salary
        expected_energy = self.worker.energy - 1
        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_increase_energy_by_resting(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_correct_info(self):
        expected_information = f'{self.worker.name} has saved {self.worker.money} money.'
        result = self.worker.get_info()

        self.assertEqual(expected_information, str(result))


if __name__ == '__main__':
    main()

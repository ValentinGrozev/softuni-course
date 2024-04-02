from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.shc = SecondHandCar("BMW", "X7", 1000, 5000.50)

    def test__init__(self):
        self.assertEqual("BMW", self.shc.model)
        self.assertEqual("X7", self.shc.car_type)
        self.assertEqual(1000, self.shc.mileage)
        self.assertEqual(5000.50, self.shc.price)
        self.assertEqual([], self.shc.repairs)

    def test_with_correct_car_price(self):
        self.assertEqual(5000.50, self.shc.price)

    def test_with_incorrect_car_price(self):
        with self.assertRaises(ValueError) as ve:
            self.shc.price = 1.0

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_with_correct_car_mileage(self):
        self.assertEqual(1000, self.shc.mileage)

    def test_with_incorrect_car_mileage(self):
        with self.assertRaises(ValueError) as ve:
            self.shc.mileage = 100

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_set_new_incorrect_and_higher_promotional_price(self):
        with self.assertRaises(ValueError) as ve:
            self.shc.set_promotional_price(15000.50)

        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_set_new_correct_and_lower_promotional_price(self):
        result = self.shc.set_promotional_price(2000.50)
        self.assertEqual("The promotional price has been successfully set.", result)

    def test_repair_case_is_impossible(self):
        result = self.shc.need_repair(4000.50, "Engine")
        self.assertEqual("Repair is impossible!", result)

    def test_repair_is_completed(self):
        result = self.shc.need_repair(400.50, "Engine")
        self.assertEqual("Price has been increased due to repair charges.", result)
        self.assertEqual(5401.00, self.shc.price)
        self.assertEqual(1, len(self.shc.repairs))

    def test_cant_compare_with_different_car(self):
        self.other_shc = SecondHandCar("Audi", "A7", 2000, 8000.50)
        result = self.shc.__gt__(self.other_shc)
        self.assertEqual("Cars cannot be compared. Type mismatch!", result)

    def test_compare_prices_between_two_cars_return_True(self):
        self.second_shc = SecondHandCar("BMW", "X7", 3000, 2000.50)
        self.assertTrue(self.shc.__gt__(self.second_shc))

    def test_compare_prices_between_two_cars_return_False(self):
        self.second_shc = SecondHandCar("BMW", "X7", 3000, 12000.50)
        self.assertFalse(self.shc.__gt__(self.second_shc))

    def test_return_information_for_car(self):
        result = self.shc.__str__()

        expected_result = f"Model {self.shc.model} | Type {self.shc.car_type} | Milage {self.shc.mileage}km\n"
        expected_result += f"Current price: {self.shc.price:.2f} | Number of Repairs: {len(self.shc.repairs)}"

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()

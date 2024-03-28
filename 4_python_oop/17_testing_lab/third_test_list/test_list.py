from unittest import TestCase, main
from extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.int_list = IntegerList(2.5, 2, 4, 6, "Me")

    def test_correct_init(self):
        self.assertEqual([2, 4, 6], self.int_list.get_data())

    def test_add_non_integer_element_in_integer_list_except_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_integer_element_in_list_expect_success(self):
        expected_result = self.int_list.get_data() + [5]
        result = self.int_list.add(5)
        self.assertEqual(expected_result, result)

    def test_remove_element_with_invalid_index_expect_index_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.remove_index(6)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_element_with_valid_index_expect_success(self):
        self.int_list.remove_index(0)
        self.assertEqual([4, 6], self.int_list.get_data())

    def test_get_item_with_invalid_index_expect_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.get(100)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_item_with_valid_index_expect_success(self):
        result = self.int_list.get(0)
        expected_result = 2
        self.assertEqual(expected_result, result)

    def test_insert_integer_element_with_invalid_index_in_list_expect_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.insert(13, 5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_non_integer_element_with_valid_index_in_list_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.insert(0, 5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_integer_element_with_valid_index_in_list_expect_success(self):
        expected_result = self.int_list.get_data().copy()
        expected_result.insert(0, 6)
        self.int_list.insert(0, 6)
        self.assertEqual(expected_result, self.int_list.get_data())

    def test_get_biggest_number(self):
        result = self.int_list.get_biggest()
        expected_result = 6
        self.assertEqual(expected_result, result)

    def test_get_index_of_element(self):
        result = self.int_list.get_index(2)
        expected_result = 0
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()

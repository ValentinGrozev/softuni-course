from unittest import TestCase, main
from project.toy_store import ToyStore


class TestToyStore(TestCase):
    def setUp(self):
        self.ts = ToyStore()

    def test__init__(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.ts.toy_shelf)

    def test_cant_add_toy_because_shelf_is_missing(self):
        with self.assertRaises(Exception) as ex:
            self.ts.add_toy("P", "Cat")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_cant_add_toy_because_already_have_the_same_toy(self):
        self.ts.add_toy("A", "Cat")

        with self.assertRaises(Exception) as ex:
            self.ts.add_toy("A", "Cat")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_cant_add_toy_because_shelf_is_already_taken(self):
        self.ts.add_toy("A", "Cat")

        with self.assertRaises(Exception) as ex:
            self.ts.add_toy("A", "Dog")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_to_a_shelf(self):
        result = self.ts.add_toy("A", "Cat")

        self.assertEqual(f"Toy:Cat placed successfully!", result)

    def test_add_toys_to_a_different_shelves(self):
        result = self.ts.add_toy("A", "Cat")
        self.assertEqual(f"Toy:Cat placed successfully!", result)

        result = self.ts.add_toy("B", "Dog")
        self.assertEqual(f"Toy:Dog placed successfully!", result)

        result = self.ts.add_toy("C", "Elephant")
        self.assertEqual(f"Toy:Elephant placed successfully!", result)

    def test_cant_remove_toy_because_shelf_is_missing(self):
        with self.assertRaises(Exception) as ex:
            self.ts.remove_toy("P", "Cat")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_cant_remove_toy_because_toy_is_not_existing(self):
        self.ts.add_toy("A", "Dog")

        with self.assertRaises(Exception) as ex:
            self.ts.remove_toy("A", "Cat")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy(self):
        self.ts.add_toy("A", "Cat")
        result = self.ts.remove_toy("A", "Cat")
        result_2 = self.ts.toy_shelf["A"]
        self.assertEqual(None, result_2)
        self.assertEqual(f"Remove toy:Cat successfully!", result)


if __name__ == "__main__":
    main()

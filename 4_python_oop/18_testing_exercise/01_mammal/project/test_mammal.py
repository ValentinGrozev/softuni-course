from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Dog", "Mammal", "Wof")

    def test__init__(self):
        self.assertEqual("Dog", self.mammal.name)
        self.assertEqual("Mammal", self.mammal.type)
        self.assertEqual("Wof", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound(self):
        expected_result = "Dog makes Wof"
        self.assertEqual(expected_result, self.mammal.make_sound())

    def test_get_kingdom(self):
        expected_result = "animals"
        self.assertEqual(expected_result, self.mammal.get_kingdom())

    def test_get_information(self):
        expected_result = "Dog is of type Mammal"
        self.assertEqual(expected_result, self.mammal.info())


if __name__ == '__main__':
    main()

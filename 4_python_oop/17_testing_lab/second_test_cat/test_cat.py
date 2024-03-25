from unittest import TestCase, main
from cat import Cat


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat("Tomi")

    def test_correct__init__(self):
        self.assertEqual("Tomi", self.cat.name)
        self.assertEqual(False, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_feed_cat_which_is_already_feed(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_feed_cat(self):
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertEqual(True, self.cat.fed)
        self.assertEqual(True, self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_cat_cant_sleep_if_hungry(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_going_to_sleep_after_sleep(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertEqual(False, self.cat.sleepy)


if __name__ == '__main__':
    main()

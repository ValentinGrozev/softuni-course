from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Batman", 1, 200, 50)
        self.enemy = Hero("Joker", 1, 200, 25)

    def test__init__(self):
        self.assertEqual("Batman", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(200, self.hero.health)
        self.assertEqual(50, self.hero.damage)

    def test_battle_with_enemy_hero_with_equal_name(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_cant_battle_with_zero_or_negative_health(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_cant_battle_when_enemy_health_is_zero_or_negative(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

    def test_battle_with_enemy_expect_result_draw(self):
        self.hero.health = 25
        self.enemy.health = 10

        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(-40, self.enemy.health)

    def test_battle_and_hero_wins(self):
        self.enemy.health = 50
        expected_hero_level = self.hero.level + 1
        expected_hero_health = self.hero.health - (self.enemy.damage * self.enemy.level) + 5
        expected_hero_damage = self.hero.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(expected_hero_level, self.hero.level)
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(expected_hero_damage, self.hero.damage)

    def test_battle_and_enemy_hero_wins(self):
        self.hero.health = 25
        expected_enemy_level = self.enemy.level + 1
        expected_enemy_health = self.enemy.health - (self.hero.damage * self.hero.level) + 5
        expected_enemy_damage = self.enemy.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(expected_enemy_level, self.enemy.level)
        self.assertEqual(expected_enemy_health, self.enemy.health)
        self.assertEqual(expected_enemy_damage, self.enemy.damage)

    def test_correct_str_representation(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"
        self.assertEqual(expected_result, self.hero.__str__())


if __name__ == "__main__":
    main()
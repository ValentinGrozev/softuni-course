from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):

    def setUp(self):
        self.player = TennisPlayer("Andy", 29, 300.50)

    def test__init__(self):
        self.assertEqual("Andy", self.player.name)
        self.assertEqual(29, self.player.age)
        self.assertEqual(300.50, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_incorrect_name(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "AA"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_under_18(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_age_exactly_18(self):
        self.player.age = 18
        self.assertEqual(18, self.player.age)

    def test_add_win_in_wins_list(self):
        self.player.add_new_win("Us open")
        self.assertEqual(1, len(self.player.wins))
        self.assertEqual(["Us open"], self.player.wins)

    def test_add_second_win_in_wins_list(self):
        self.player.add_new_win("Us open")
        self.player.add_new_win("French open")
        self.assertEqual(2, len(self.player.wins))
        self.assertEqual(["Us open", "French open"], self.player.wins)

    def test_cant_add_win_because_tournament_is_in_wins_list(self):
        self.player.add_new_win("Us open")
        result = self.player.add_new_win("Us open")
        self.assertEqual(1, len(self.player.wins))
        self.assertEqual("Us open has been already added to the list of wins!", result)

    def test_compare_with_player_with_more_points(self):
        self.other_player = TennisPlayer("Novak", 29, 500.50)
        result = self.player.__lt__(self.other_player)
        exp_result = f'{self.other_player.name} is a top seeded player and he/she is better than {self.player.name}'
        self.assertEqual(exp_result, result)

    def test_compare_with_player_with_lower_points(self):
        self.other_player = TennisPlayer("Novak", 29, 100.50)
        result = self.player.__lt__(self.other_player)
        expected_result = f'{self.player.name} is a better player than {self.other_player.name}'
        self.assertEqual(expected_result, result)

    def test_compare_players_with_equal_points(self):
        self.other_player = TennisPlayer("Novak", 29, 300.50)
        result = self.player.__lt__(self.other_player)
        expected_result = f'{self.player.name} is a better player than {self.other_player.name}'
        self.assertEqual(expected_result, result)

    def test__str__without_win(self):
        result = str(self.player)
        expected_result = f"Tennis Player: {self.player.name}\n" \
                          f"Age: {self.player.age}\n" \
                          f"Points: {self.player.points:.1f}\n" \
                          f"Tournaments won: {', '.join(self.player.wins)}"

        self.assertEqual(expected_result, result)

    def test__str___with_one_win(self):
        self.player.add_new_win("Us open")
        result = str(self.player)
        expected_result = f"Tennis Player: {self.player.name}\n" \
                          f"Age: {self.player.age}\n" \
                          f"Points: {self.player.points:.1f}\n" \
                          f"Tournaments won: {', '.join(self.player.wins)}"

        self.assertEqual(expected_result, result)

    def test__str___with_two_wins(self):
        self.player.add_new_win("Us open")
        self.player.add_new_win("French open")
        result = str(self.player)
        expected_result = f"Tennis Player: {self.player.name}\n" \
                          f"Age: {self.player.age}\n" \
                          f"Points: {self.player.points:.1f}\n" \
                          f"Tournaments won: {', '.join(self.player.wins)}"

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()

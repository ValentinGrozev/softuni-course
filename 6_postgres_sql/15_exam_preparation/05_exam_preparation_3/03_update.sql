UPDATE players_ranges
	SET max_players = max_players + 1
		WHERE id = (SELECT
					id
				FROM
					players_ranges
				WHERE
					min_players = 2
						and
					max_players = 2);


UPDATE board_games
	SET name = CONCAT(name, ' V2')
		WHERE id in (SELECT
					id
				FROM
					board_games
				WHERE
					release_year >= 2020);
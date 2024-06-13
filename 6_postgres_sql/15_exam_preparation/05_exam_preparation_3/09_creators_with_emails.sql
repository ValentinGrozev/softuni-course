SELECT
	CONCAT(c.first_name, ' ', c.last_name) AS full_name,
	c.email,
	MAX(b.rating)
FROM
	creators AS c
JOIN
	creators_board_games AS cb
		ON cb.creator_id = c.id
			JOIN
				board_games AS b
					ON cb.board_game_id = b.id
GROUP BY
	CONCAT(c.first_name, ' ', c.last_name),
	c.email
HAVING
	c.email LIKE '%.com'
    
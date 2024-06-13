SELECT
	c.last_name,
	CEIL(AVG(b.rating)) AS average_rating,
	p.name AS publisher_name
FROM
	board_games AS b
JOIN
	publishers AS p
		ON b.publisher_id = p.id
			JOIN creators_board_games AS cb
				ON b.id = cb.board_game_id
					JOIN
						creators AS c
							ON c.id = cb.creator_id
WHERE
	p.name = 'Stonemaier Games'
GROUP BY
	c.last_name,
	p.name
ORDER BY
	AVG(b.rating) DESC
    
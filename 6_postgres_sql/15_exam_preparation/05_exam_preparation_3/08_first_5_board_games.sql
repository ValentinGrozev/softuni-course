SELECT
	b.name,
	b.rating,
	c.name
FROM
	board_games AS b
JOIN
	categories AS c
		ON b.category_id = c.id
			JOIN 
				players_ranges AS pr
					ON pr.id = b.players_range_id
WHERE
	(b.rating > 7.00 and b.name ILIKE '%a%')
		OR
	(b.rating > 7.50 and ((pr.min_players + pr.min_players) BETWEEN 2 and 5))
ORDER BY
	b.name,
	b.rating DESC
LIMIT 5

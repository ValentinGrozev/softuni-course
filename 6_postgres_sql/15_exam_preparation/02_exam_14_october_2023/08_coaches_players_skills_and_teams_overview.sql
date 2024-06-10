SELECT
	CONCAT(c.first_name, ' ', c.last_name) AS coach_full_name,
	CONCAT(p.first_name, ' ', p.last_name) AS player_full_name,
	t.name AS team_name,
	sd.passing,
	sd.shooting,
	sd.speed
FROM
	players AS p
JOIN
	players_coaches AS pc
		ON pc.player_id = p.id
			JOIN
				coaches AS c
					ON pc.coach_id = c.id
						JOIN
							teams AS t
								ON p.team_id = t.id
									JOIN
										skills_data AS sd
											on sd.id = p.skills_data_id
ORDER BY
	coach_full_name,
	player_full_name DESC									
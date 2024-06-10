UPDATE coaches
	SET salary = salary * coach_level
		WHERE 
			SUBSTRING(first_name, 1, 1) = 'C'
				and
			id in (SELECT coach_id FROM players_coaches)
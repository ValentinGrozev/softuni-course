UPDATE projects
	SET end_date = start_date + INTERVAL '5' month

WHERE
	end_date is NULL
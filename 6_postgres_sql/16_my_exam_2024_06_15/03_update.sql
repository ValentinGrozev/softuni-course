UPDATE addresses
	SET country = (SELECT 
			CASE 
				WHEN country LIKE 'B%' THEN 'Blocked'
				WHEN country LIKE 'T%' THEN 'Test'
				WHEN country LIKE 'P%' THEN 'In Progress'
				ELSE country
				END)

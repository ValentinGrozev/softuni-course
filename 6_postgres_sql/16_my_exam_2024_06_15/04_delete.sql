DELETE FROM addresses
	WHERE
		id in (SELECT
				id
			FROM
				addresses
			WHERE
				id % 2 = 0 
					and 
				street LIKE '%r%')
                
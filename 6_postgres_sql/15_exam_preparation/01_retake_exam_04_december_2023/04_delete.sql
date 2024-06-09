DELETE FROM distributors
WHERE 
	LOWER(SUBSTRING(name, 1, 1)) = 'l'
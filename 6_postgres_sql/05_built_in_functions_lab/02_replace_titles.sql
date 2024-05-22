UPDATE books
SET
	title = REPLACE(title, (SUBSTRING(title, 1, 3)), '***')
WHERE
	SUBSTRING(title, 1, 3) = 'The'
RETURNING title
SELECT
	first_name,
	last_name,
	EXTRACT('Year'from born)
FROM
	authors
SELECT
	last_name,
	COUNT(notes) AS notes_with_dumbledore
FROM
	wizard_deposits
WHERE
	notes LIKE '%Dumbledore%'
GROUP bY
	last_name
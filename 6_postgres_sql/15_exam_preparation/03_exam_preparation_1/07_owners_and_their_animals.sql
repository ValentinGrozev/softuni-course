SELECT
	o.name,
	COUNT(*) AS count_of_animals
FROM
	owners AS o
JOIN
	animals AS a
		ON o.id = a.owner_id
GROUP BY
	o.name 
ORDER BY
	COUNT(*) DESC,
	o.name
LIMIT 5

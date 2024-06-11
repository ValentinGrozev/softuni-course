SELECT
	a.name,
	EXTRACT(YEAR FROM a.birthdate),
	at.animal_type
FROM
	animals AS a
JOIN
	animal_types AS at
		ON a.animal_type_id = at.id
WHERE
	at.animal_type <> 'Birds'
		and
	a.birthdate > DATE '01/01/2022' - INTERVAL '5 years'
		and
	a.owner_id IS NULL
ORDER BY
	name
    
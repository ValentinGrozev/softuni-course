SELECT
	v.name,
	v.phone_number,
	TRIM('Sofia , ' FROM v.address) AS address
FROM
	volunteers AS v
JOIN
	volunteers_departments AS vd
		ON vd.id = v.department_id
WHERE
	vd.department_name = 'Education program assistant'
		AND
	v.address ILIKE '%Sofia%'
ORDER BY
	v.name,
	v.phone_number,
	v.address
    
--First solution with TO_CHAR

SELECT
	a.name AS address,
		CASE 
			WHEN TO_CHAR(start, 'HH24')::int BETWEEN 6 and 20 THEN 'Day'
			ELSE 'Night' END AS day_time,
	cou.bill,
	c.full_name,
	ca.make,
	ca.model,
	cat.name AS category_name
FROM
	addresses AS a
JOIN
	courses AS cou
		ON a.id = cou.from_address_id
			JOIN 
				clients AS c
					ON c.id = cou.client_id
						JOIN cars AS ca
							ON ca.id = cou.car_id
								JOIN categories AS cat
									ON cat.id = ca.category_id
ORDER BY
	cou.id


-- Second solution with Extract 

SELECT
	a.name AS address,
		CASE 
			WHEN EXTRACT(HOURS FROM cou.start) BETWEEN 6 AND 20 THEN 'Day'
       		ELSE 'Night' END AS day_time,
	cou.bill,
	c.full_name,
	ca.make,
	ca.model,
	cat.name AS category_name
FROM
	addresses AS a
JOIN
	courses AS cou
		ON a.id = cou.from_address_id
			JOIN 
				clients AS c
					ON c.id = cou.client_id
						JOIN cars AS ca
							ON ca.id = cou.car_id
								JOIN categories AS cat
									ON cat.id = ca.category_id
ORDER BY
	cou.id

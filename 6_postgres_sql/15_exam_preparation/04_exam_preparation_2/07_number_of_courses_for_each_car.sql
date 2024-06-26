SELECT
	c.id AS car_id,
	c.make,
	c.mileage,
	COUNT(cou.car_id) AS count_of_courses,
	ROUND(AVG(cou.bill), 2) AS average_bill
FROM
	cars AS c
LEFT JOIN
	courses AS cou
		ON c.id = cou.car_id
GROUP BY
	c.id,
	c.make,
	c.mileage
HAVING
	COUNT(cou.car_id) <> 2
ORDER BY
	COUNT(cou.car_id) DESC,
	c.id
    
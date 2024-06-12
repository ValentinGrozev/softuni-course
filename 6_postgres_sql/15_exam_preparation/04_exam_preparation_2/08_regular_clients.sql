SELECT
	c.full_name,
	COUNT(cou.client_id) AS count_of_cars,
	SUM(cou.bill) AS total_sum
FROM
	clients AS c
JOIN
	courses AS cou
		ON c.id = cou.client_id
GROUP BY
	c.full_name
HAVING
	c.full_name LIKE '_a%' and
	COUNT(cou.client_id) > 1
ORDER BY
	c.full_name
    
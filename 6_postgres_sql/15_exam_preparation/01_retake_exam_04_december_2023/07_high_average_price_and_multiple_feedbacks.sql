SELECT
	p.name AS product_name,
	ROUND(AVG(p.price), 2) AS average_price,
	COUNT(p.id) AS total_feedbacks
FROM
	products AS p
JOIN
	feedbacks AS f
		ON p.id = f.product_id
WHERE
	p.price > 15
GROUP BY
	p.name
HAVING
 	COUNT(p.id) > 1
ORDER BY
	COUNT(p.id) 
    
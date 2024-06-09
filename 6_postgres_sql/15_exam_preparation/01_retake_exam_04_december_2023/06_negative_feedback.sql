SELECT
	f.product_id,
	f.rate,
	f.description,
	f.customer_id,
	c.age,
	c.gender
FROM
	customers AS c
JOIN
	feedbacks AS f
		ON c.id = f.customer_id
WHERE
	f.rate < 5 and 
	c.gender in ('F') 
	and c.age > 30
ORDER BY
	f.product_id DESC

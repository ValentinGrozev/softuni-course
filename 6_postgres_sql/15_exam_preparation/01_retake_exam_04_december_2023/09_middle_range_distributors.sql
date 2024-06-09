SELECT
	d.name AS distributor_name,
	i.name AS ingredient_name,
	p.name AS product_name,
	AVG(f.rate) AS average_rate
FROM
	ingredients AS i
JOIN
	products_ingredients AS pi
		ON i.id = pi.ingredient_id
			JOIN products AS p
				ON p.id = pi.product_id
					JOIN distributors AS d
						ON d.id = i.distributor_id
							JOIN feedbacks as f
								ON p.id = f.product_id
GROUP BY
	d.name,
	i.name,
	p.name
HAVING
	AVG(f.rate) BETWEEN 5 and 8
ORDER BY
	distributor_name,
	ingredient_name,
	product_name
    
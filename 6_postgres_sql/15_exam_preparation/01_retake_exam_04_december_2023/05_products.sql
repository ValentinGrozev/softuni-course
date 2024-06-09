SELECT
	name,
	recipe,
	price
FROM
	products
WHERE price between 10 and 20
ORDER BY
	price DESC
    
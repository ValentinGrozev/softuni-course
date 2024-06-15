SELECT
	p.id,
	p.capture_date,
	p.description,
	COUNT(c.photo_id) AS comments_count
FROM
	photos AS p
JOIN
	comments AS c
		ON p.id = c.photo_id
GROUP BY
	p.id,
	p.capture_date,
	p.description
HAVING
	p.description IS NOT NULL
ORDER BY
	COUNT(c.photo_id) DESC,
	p.id
LIMIT 3

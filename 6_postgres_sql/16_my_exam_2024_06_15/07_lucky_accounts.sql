SELECT
	CONCAT(a.id, ' ', a.username) AS id_username,
	a.email
FROM
	accounts AS a
JOIN
	accounts_photos AS ac
		ON a.id = ac.account_id
WHERE
	ac.account_id = ac.photo_id
    
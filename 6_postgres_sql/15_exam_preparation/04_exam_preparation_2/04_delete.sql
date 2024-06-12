DELETE FROM clients
	WHERE
		clients.id in (SELECT
							c.id
						FROM
							clients AS c
						LEFT JOIN
							courses AS cour
								ON c.id = cour.client_id
						WHERE
							cour.client_id IS NULL and
							LENGTH(full_name) > 3
						);
CREATE OR REPLACE PROCEDURE
	udp_modify_account(address_street VARCHAR(30), address_town VARCHAR(30))
AS
$$
BEGIN
	UPDATE accounts
		SET job_title = CONCAT('(Remote) ',job_title)
			WHERE
				id in (SELECT
							account_id
						FROM
							accounts AS a
						JOIN
							addresses AS ad
								ON ad.account_id = a.id
						WHERE
							ad.street = address_street
								and
							ad.town = address_town);
END;
$$
LANGUAGE plpgsql

CREATE OR REPLACE PROCEDURE 
	sp_customer_country_name(IN customer_full_name VARCHAR(50), INOUT country_name VARCHAR(50))
AS
$$
BEGIN
	SELECT
		cou.name INTO country_name
	FROM
		customers AS c
	JOIN
		countries AS cou
			ON c.country_id = cou.id
	WHERE
		CONCAT(c.first_name, ' ', c.last_name) = customer_full_name;
	RETURN;
END;
$$
LANGUAGE plpgsql

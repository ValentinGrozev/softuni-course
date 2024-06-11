CREATE OR REPLACE PROCEDURE	
	sp_animals_with_owners_or_not(
	IN animal_name VARCHAR(30), 
	OUT result_info VARCHAR(30)
	)
AS
$$
BEGIN
	SELECT
		o.name INTO result_info
	FROM
		owners AS o
	JOIN
		animals AS a
			ON o.id = a.owner_id
	WHERE
		a.name = animal_name;

	IF result_info IS null THEN
		result_info = 'For adoption';
	END IF;
END;
$$
LANGUAGE plpgsql

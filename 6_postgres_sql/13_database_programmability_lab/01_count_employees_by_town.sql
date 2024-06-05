CREATE OR REPLACE FUNCTION
	fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT 
AS
$$
DECLARE
	counter INT;
BEGIN
	SELECT
		count(*) INTO counter
	FROM
		employees AS e
	JOIN
		addresses AS a
			using(address_id)
				JOIN towns AS t
					USING(town_id)
	WHERE
		t.name = town_name;
	RETURN counter;
END;
$$
LANGUAGE plpgsql
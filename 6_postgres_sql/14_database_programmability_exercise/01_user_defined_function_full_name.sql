CREATE OR REPLACE FUNCTION
	fn_full_name(first_name VARCHAR(30), last_name VARCHAR(30))
RETURNS VARCHAR(61)
AS
$$	
	BEGIN
		RETURN CONCAT(
			INITCAP(first_name), 
			' ', 
			INITCAP(last_name)
	) AS full_name;
	END;
$$
LANGUAGE plpgsql

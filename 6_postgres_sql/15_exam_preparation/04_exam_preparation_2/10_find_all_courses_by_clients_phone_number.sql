CREATE OR REPLACE FUNCTION
	fn_courses_by_client(phone_num VARCHAR(20))
RETURNS INT
AS
$$
BEGIN
	RETURN(
	SELECT
		COUNT(*)
	FROM
		clients AS c
	JOIN
		courses AS cou
			ON c.id = cou.client_id
	WHERE
		c.phone_number = phone_num);
END;
$$
LANGUAGE plpgsql


-- Call the function
SELECT fn_courses_by_client('(803) 6386812')
-- Expected result: 5

-- Call the function
SELECT fn_courses_by_client('(831) 1391236')
-- Expected result: 3

-- Call the function
SELECT fn_courses_by_client('(704) 2502909')
-- Expected result: 0
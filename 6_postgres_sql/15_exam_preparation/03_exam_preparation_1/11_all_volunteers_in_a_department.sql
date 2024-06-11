CREATE OR REPLACE FUNCTION
	fn_get_volunteers_count_from_department(searched_volunteers_department VARCHAR(30))
RETURNS INT
AS
$$
BEGIN
	RETURN(
	SELECT
		COUNT(*)
	FROM
		volunteers AS v
	JOIN
		volunteers_departments as vd
			ON v.department_id = vd.id
	WHERE
		vd.department_name = searched_volunteers_department);
END;
$$
LANGUAGE plpgsql

-- Call the function
SELECT fn_get_volunteers_count_from_department('Education program assistant')

-- Expected result
6

-- Call the function
SELECT fn_get_volunteers_count_from_department('Guest engagement')

-- Expected result
4

-- Call the function
SELECT fn_get_volunteers_count_from_department('Zoo events')

-- Expected result
5
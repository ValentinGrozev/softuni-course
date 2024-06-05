CREATE OR REPLACE PROCEDURE sp_increase_salaries(department_name VARCHAR(30))
AS
$$
BEGIN
	UPDATE employees AS e
		SET salary = salary * 1.05
	WHERE e.department_id = (
		SELECT 
			department_id 
		FROM 
			departments AS d
		WHERE 
			d.name = department_name);
END;
$$
LANGUAGE plpgsql


-- Steps to use the procedure and see the result

-- CALL sp_increase_salaries('Finance')

/*
SELECT
	e.first_name,
	e.salary
FROM
	employees AS e
JOIN
	departments AS d
		USING(department_id)
WHERE
	d.name = 'Finance'
ORDER BY
	first_name
*/
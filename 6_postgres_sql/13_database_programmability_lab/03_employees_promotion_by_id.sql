CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(id INT)
AS
$$
BEGIN
	IF 1 <> (SELECT COUNT(employee_id) FROM employees WHERE employee_id = id) THEN
		ROLLBACK;
	ELSE
		UPDATE employees AS e
			SET salary = salary * 1.05
		WHERE 
			employee_id = id;
	END IF;
END;
$$
LANGUAGE plpgsql

-- Steps to use the procedure and see the result

-- CALL sp_increase_salary_by_id(17)

-- SELECT salary from employees WHERE employee_id = 17
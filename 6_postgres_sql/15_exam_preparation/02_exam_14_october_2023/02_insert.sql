UPDATE players
	SET salary = salary * 2
	WHERE
		hire_date < '2013-12-13 07:18:46';

INSERT INTO coaches(first_name, last_name, salary, coach_level)	
	SELECT
		first_name,
		last_name,
		ROUND(salary, 2),
		LENGTH(first_name)
	FROM
		players
	WHERE
		hire_date < '2013-12-13 07:18:46';
        
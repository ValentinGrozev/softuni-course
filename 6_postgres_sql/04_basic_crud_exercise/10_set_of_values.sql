SELECT
	employee_id,
	project_id

FROM employees_projects
WHERE 
	employee_id in (200, 250)
	and project_id not in (50, 100)
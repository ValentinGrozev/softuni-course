CREATE TABLE employees_projects(
	id SERIAL PRIMARY KEY, 
	employee_id int REFERENCES employees(id),
	project_id int REFERENCES projects(id)
)
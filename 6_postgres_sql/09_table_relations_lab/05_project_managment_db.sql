CREATE TABLE clients(
	id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name VARCHAR (10)
	);

CREATE TABLE employees(
	id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	first_name VARCHAR (30),
	last_name VARCHAR (30),
	project_id INT
	);
	
CREATE TABLE projects(
	id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	client_id INT,
	project_lead_id INT,

	CONSTRAINT fk_client_id_id
	FOREIGN KEY (client_id)
	REFERENCES clients(id),

	CONSTRAINT fk_project_lead_id_employees
	FOREIGN KEY (project_lead_id)
	REFERENCES employees(id)
);

ALTER TABLE employees
	ADD CONSTRAINT fk_employees_projects
		FOREIGN KEY (project_id)
		REFERENCES projects(id)
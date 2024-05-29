CREATE TABLE
	mountains(
	id SERIAL PRIMARY KEY,
	name VARCHAR (30)
	);

CREATE TABLE
	peaks(
	id SERIAL PRIMARY KEY,
	name VARCHAR (30),
	mountain_id INT,

	CONSTRAINT fk_mountain_id
	FOREIGN KEY (mountain_id)
	REFERENCES mountains(id)
	ON DELETE CASCADE
	);
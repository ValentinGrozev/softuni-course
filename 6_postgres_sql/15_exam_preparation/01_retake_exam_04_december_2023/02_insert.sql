CREATE TABLE gift_recipients(
	id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name VARCHAR(100),
	country_id INT,
	gift_sent BOOLEAN DEFAULT FALSE
);

INSERT INTO gift_recipients(name, country_id)
SELECT
	CONCAT(c.first_name, ' ', c.last_name),
	c.country_id
FROM 
	customers AS c;

UPDATE gift_recipients
	SET gift_sent = True
		WHERE country_id in (7, 8, 14, 17, 26);
        
CREATE TABLE search_results (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    release_year INT,
    rating FLOAT,
    category_name VARCHAR(50),
    publisher_name VARCHAR(50),
    min_players VARCHAR(50),
    max_players VARCHAR(50)
);

CREATE OR REPLACE PROCEDURE
	usp_search_by_category(category VARCHAR(50))
AS
$$
BEGIN
	insert INTO 
		search_results(
			name,
			release_year,
			rating,
			category_name,
			publisher_name,
			min_players,
			max_players
	)
	SELECT	
		b.name,
		b.release_year,
		b.rating,
		c.name AS category_name,
		p.name AS publisher_name,
		CONCAT(pr.min_players, ' people') AS min_players,
		CONCAT(pr.max_players, ' people') AS max_players
	FROM
		board_games AS b
	JOIN
		categories AS c
			ON b.category_id = c.id
				JOIN publishers AS p
					ON p.id = b.publisher_id
						JOIN players_ranges AS pr
							ON b.players_range_id = pr.id
	WHERE
		c.name = category
	ORDER BY
		p.name,
		b.release_year DESC;
END;
$$
LANGUAGE plpgsql

CREATE OR REPLACE FUNCTION
	fn_stadium_team_name(stadium_name VARCHAR(30))
RETURNS TABLE(
	teams_name VARCHAR(50)
)
AS
$$
BEGIN
	RETURN QUERY(
		SELECT
			t.name 
		FROM
			stadiums AS s
		JOIN
			teams AS t
				ON s.id = t.stadium_id
		WHERE
			s.name = stadium_name)
		ORDER BY
			t.name;
END;
$$
LANGUAGE plpgsql

-- Call the function
SELECT fn_stadium_team_name('Jaxworks')

/* Expected result
    Ailane
    Feedmix
    Jabbercube
    Skipstorm
    */
    
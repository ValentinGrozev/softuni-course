CREATE OR REPLACE PROCEDURE
	sp_players_team_name(player_name VARCHAR(50), INOUT team_name VARCHAR(45))
AS
$$
BEGIN
	team_name = (
		SELECT
			t.name
		FROM
			players AS p
		JOIN
			teams AS t
				ON p.team_id = t.id
		WHERE
			CONCAT(p.first_name, ' ', p.last_name) = player_name);
	if team_name IS NULL THEN
		team_name = 'The player currently has no team';
	ELSE
		RETURN;
	END IF;
END;
$$
LANGUAGE plpgsql

-- Call the procedure
CALL sp_players_team_name('Thor Serrels', '')
-- Expected result: Ntags

-- Call the procedure
CALL sp_players_team_name('Walther Olenchenko', '')
-- Expected result: The player currently has no team

-- Call the procedure
CALL sp_players_team_name('Isaak Duncombe', '')
-- Expected result: Thoughtstorm
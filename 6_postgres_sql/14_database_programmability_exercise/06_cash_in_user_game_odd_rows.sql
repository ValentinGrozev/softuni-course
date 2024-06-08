CREATE OR REPLACE FUNCTION 
	fn_cash_in_users_games(game_name VARCHAR(50))
RETURNS TABLE(
	total_cash NUMERIC
)
AS
$$
BEGIN
	RETURN QUERY
	WITH GAMES_INFO AS (
		SELECT
			ROW_NUMBER() OVER(ORDER BY ug.cash DESC) AS row_index,
			g.name,
			ug.cash
		FROM
			users_games AS ug
		JOIN
			games AS g
				ON ug.game_id = g.id
		WHERE
			g.name = game_name
	)

	SELECT
		ROUND(SUM(cash), 2) AS total_cash
	FROM
		GAMES_INFO AS GI
	WHERE
		GI.row_index % 2 <> 0;
END;
$$
LANGUAGE plpgsql
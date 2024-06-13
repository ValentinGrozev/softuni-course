CREATE OR REPLACE FUNCTION
	fn_creator_with_board_games(first_name_of_creator  VARCHAR(30))
RETURNS INT
AS
$$
BEGIN
	RETURN(
		SELECT
			COUNT(*)
		FROM
			creators AS c
		JOIN
			creators_board_games AS cb
				ON c.id = cb.creator_id
		WHERE
			cb.creator_id in (SELECT
									id
								FROM 
									creators
								WHERE
									first_name = first_name_of_creator)
	);
END;
$$
LANGUAGE plpgsql


-- Call the function
SELECT fn_creator_with_board_games('Bruno') 

-- Expected result: 13

-- Call the function
SELECT fn_creator_with_board_games('Alexander')

-- Expected result: 19
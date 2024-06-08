CREATE OR REPLACE PROCEDURE
	sp_retrieving_holders_with_balance_higher_than(searched_balance NUMERIC)
AS
$$
DECLARE
	holder_account_info RECORD;
BEGIN
	FOR holder_account_info IN
		SELECT
			CONCAT(ah.first_name, ' ', ah.last_name) AS full_name,
			sum(a.balance) AS total_balance
		FROM
			account_holders AS ah
		JOIN
			accounts AS a
				ON ah.id = a.account_holder_id
		GROUP BY
			full_name
		HAVING
			sum(a.balance) > searched_balance
		ORDER BY
			full_name
	LOOP
		RAISE NOTICE '% - %', holder_account_info.full_name, holder_account_info.total_balance;
	END LOOP;
END;
$$
LANGUAGE plpgsql


-- Call the procedure
CALL sp_retrieving_holders_with_balance_higher_than(20000)

CREATE OR REPLACE PROCEDURE
	sp_deposit_money(account_id INT, money_amount NUMERIC (10, 4))
AS
$$
BEGIN
	UPDATE accounts
		SET balance = balance + money_amount 
	WHERE
		id = account_id;
END;
$$
LANGUAGE plpgsql

-- Call the procedure
CALL sp_deposit_money(14, 1000)

--Select and check the result
SELECT
	*
FROM
	accounts
WHERE
	accounts.id = 14

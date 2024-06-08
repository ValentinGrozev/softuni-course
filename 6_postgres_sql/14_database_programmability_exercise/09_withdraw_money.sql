CREATE OR REPLACE PROCEDURE
	sp_withdraw_money(account_id INT, money_amount NUMERIC (4))
AS
$$
DECLARE
	current_balance NUMERIC;
BEGIN
	current_balance := (SELECT accounts.balance FROM accounts WHERE accounts.id = account_id);

	IF current_balance - money_amount >= 0 THEN
		UPDATE accounts
			SET balance = balance - money_amount
		WHERE
			accounts.id = account_id;
	ELSE
		RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
	END IF;
END;
$$
LANGUAGE plpgsql

-- Call the procedure
CALL sp_withdraw_money(3, 5050.7500)

--Select and check the result
SELECT
	*
FROM
	accounts
WHERE
	accounts.id = 3
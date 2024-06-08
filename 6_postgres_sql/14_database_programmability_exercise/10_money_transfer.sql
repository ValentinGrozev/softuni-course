CREATE OR REPLACE PROCEDURE
	sp_transfer_money(sender_id INT, receiver_id INT, amount NUMERIC(4))
AS
$$
DECLARE
	sender_money_after_transaction NUMERIC;
	reciever_money_before_transaction NUMERIC;
	reciever_money_after_transaction NUMERIC;
BEGIN
	SELECT 
			balance INTO reciever_money_before_transaction
		FROM
			accounts
		where 
			accounts.id = receiver_id;
		
	CALL sp_withdraw_money(sender_id, amount);
	CALL sp_deposit_money(receiver_id, amount);
		
		SELECT 
			balance INTO sender_money_after_transaction
		FROM
			accounts
		where 
			accounts.id = sender_id;

		IF sender_money_after_transaction < 0 THEN
			ROLLBACK;

		SELECT 
			balance INTO reciever_money_after_transaction
		FROM
			accounts
		where 
			accounts.id = receiver_id;

		ELSIF (SELECT balance FROM accounts WHERE accounts.id = receiver_id) <> reciever_money_after_transaction THEN
			ROLLBACK;
		END IF;
END;
$$
LANGUAGE plpgsql

-- Call the procedure
CALL sp_transfer_money(5, 1, 5000.0000)

--Select and check the result
SELECT 
	*
FROM
	accounts
WHERE
	accounts.id in (1, 5)
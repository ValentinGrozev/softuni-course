SELECT
	MIN(deposit_charge) AS minimum_deposit_charge
FROM
	wizard_deposits


-- Second option
SELECT
	deposit_charge
FROM
	wizard_deposits
ORDER BY
	deposit_charge
LIMIT 1
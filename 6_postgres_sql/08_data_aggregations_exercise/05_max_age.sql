SELECT
	MAX(age) AS maximum_age
FROM
	wizard_deposits

-- Second option
SELECT
	age as maximum_age
FROM
	wizard_deposits
ORDER BY
	age DESC
LIMIT 1
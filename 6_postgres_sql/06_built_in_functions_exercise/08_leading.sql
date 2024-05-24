SELECT
	continent_name,
	TRIM(continent_name) as trim
FROM 
	continents

-- Second option
SELECT
	continent_name,
	TRIM(LEADING FROM continent_name) AS "trim"
FROM
	continents;
SELECT
	continent_name,
	TRIM(TRAILING from continent_name) as trim
FROM 
	continents
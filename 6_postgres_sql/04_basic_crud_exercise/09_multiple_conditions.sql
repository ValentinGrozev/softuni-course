SELECT
	number,
	street

FROM addresses
WHERE 
	id between 50 and 100
	or number < 1000
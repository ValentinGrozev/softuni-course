SELECT
		MIN(average_area_for_continent) AS min_average_area
FROM (
		SELECT
		continent_code,
		AVG(area_in_sq_km) AS average_area_for_continent
	FROM
		countries
	GROUP BY
		continent_code
) AS area_in_sq_km
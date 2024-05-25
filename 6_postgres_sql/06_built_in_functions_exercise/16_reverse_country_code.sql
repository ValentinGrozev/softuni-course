UPDATE countries
	SET country_code = REVERSE(LOWER(LEFT(country_code, 2)))
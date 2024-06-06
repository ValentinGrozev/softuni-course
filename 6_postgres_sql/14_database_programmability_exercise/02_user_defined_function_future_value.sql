CREATE OR REPLACE FUNCTION
	fn_calculate_future_value(initial_sum INT, yearly_interest_rate DECIMAL(10, 2), number_of_years INT)
RETURNS DECIMAL(10, 4)
AS
$$
	DECLARE
		future_value DECIMAL(10, 4);
	BEGIN
		SELECT TRUNC(initial_sum * POWER((1 + yearly_interest_rate), number_of_years), 4) INTO future_value;
		RETURN future_value;
	END;
$$
LANGUAGE plpgsql

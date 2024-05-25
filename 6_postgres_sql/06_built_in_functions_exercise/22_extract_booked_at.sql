SELECT
	EXTRACT(Year FROM booked_at) AS YEAR,
	EXTRACT(Month FROM booked_at) AS Month,
	EXTRACT(Day FROM booked_at) AS Day,
	EXTRACT(Hour FROM booked_at AT TIME ZONE 'UTC') AS Hour,
	EXTRACT(Minute FROM booked_at) AS Minute,
	CEILING(EXTRACT(Second FROM booked_at)) AS Second
FROM bookings
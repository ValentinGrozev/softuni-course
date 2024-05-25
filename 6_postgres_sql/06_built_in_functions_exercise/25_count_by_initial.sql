SELECT	
	LEFT(first_name, 2) as initials,
	COUNT(*) as user_count
FROM
	users
GROUP BY initials
ORDER BY 
	user_count DESC,
	initials
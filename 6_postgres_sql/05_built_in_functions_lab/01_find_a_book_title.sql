SELECT
	title
FROM books
WHERE 
	SUBSTRING(title, 1, 3) = 'The'

/*
Second solution
SELECT
	title
FROM books
WHERE 
	LEFT(title, 3) = 'The'
    */
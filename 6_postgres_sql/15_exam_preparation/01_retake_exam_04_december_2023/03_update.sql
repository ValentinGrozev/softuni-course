UPDATE products
	SET price = price * 1.10
	
	WHERE 
		products.id in (SELECT 
				product_id 
			FROM
				feedbacks
			WHERE
				rate > 8)
                
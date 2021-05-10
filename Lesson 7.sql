use shop;

 INSERT INTO
 	orders(user_id)
 VALUES
 	(1),
 	(3),  
 	(4); 

 INSERT INTO
 	orders_products(order_id, product_id)
 VALUES
 	(1, 1),
 	(1, 1);  

 INSERT INTO
 	orders_products(order_id, product_id)
 VALUES
 	(1, 1),
 	(1, 2);
 
 INSERT INTO
 	orders_products(order_id, product_id)
 VALUES
 	(2, 1),
 	(2, 2);

 INSERT INTO
 	orders_products(order_id, product_id, total)
 VALUES
 	(4, 1, 1),
 	(4, 4, 3),
 	(4, 5, 2);


-- task 1
SELECT 
	u.id AS user_id, u.name,
	o.id AS order_id
FROM 
	users AS u
RIGHT JOIN
	orders AS o 
ON
	u.id = o.user_id;

-- task 2

SELECT 
	p.id, p.name, p.price,
	c.id AS cat_id,
	c.name AS catalog
FROM
	products AS p
JOIN
	catalogs AS c
ON 
	p.catalog_id = c.id; 
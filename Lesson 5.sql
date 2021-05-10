use shop;

 Операторы, фильтрация, сортировка и ограничение
 task 1

UPDATE products
    SET created_at = NOW() where created_at is NULL;

UPDATE products
    SET updated_at = NOW() where updated_at is null;

 task 2
    
ALTER TABLE products 
    CHANGE COLUMN `created_at` `created_at` VARCHAR(256) NULL,
    CHANGE COLUMN `updated_at` `updated_at` VARCHAR(256) NULL;

describe products;
SELECT created_at from products;

ALTER TABLE products 
    CHANGE COLUMN `created_at` `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    CHANGE COLUMN `updated_at` `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

describe products;
SELECT created_at from products;


 task 3

INSERT INTO
    storehouses_products (storehouse_id, product_id, value)
VALUES
    (1, 1, 150),
    (1, 3, 200),
    (1, 5, 100),
    (1, 7, 50),
    (1, 8, 0);

SELECT value from storehouses_products ORDER BY IF(value > 0, 0, 1), value;
   
 task 4
SELECT
    name, birthday_at, 
    CASE 
        WHEN DATE_FORMAT(birthday_at, '%m') = 05 THEN 'may'
        WHEN DATE_FORMAT(birthday_at, '%m') = 08 THEN 'august'
    END AS month_of_birth
FROM
    users WHERE DATE_FORMAT(birthday_at, '%m') = 05 OR DATE_FORMAT(birthday_at, '%m') = 08;

 task 5
SELECT* FROM catalogs WHERE id IN (3, 1, 2) ORDER BY FIELD(id, 3, 1, 2)

 Агрегация данных
 task 1
SELECT ROUND(AVG((TO_DAYS(NOW()) - TO_DAYS(birthday_at)) / 365), 0) AS AVG_Age FROM users;

 task 2
SELECT
    DAYNAME(CONCAT(YEAR(NOW()), '-', SUBSTRING(birthday_at, 6, 10))) AS week_day_of_birthday_in_this_Year,
    COUNT(*) AS amount_of_birthday
FROM
    users
GROUP BY 
    week_day_of_birthday_in_this_Year
ORDER BY
	amount_of_birthday DESC;
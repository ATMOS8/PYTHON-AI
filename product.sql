CREATE TABLE product (
	id				INT PRIMARY KEY,
    date			DATE NOT NULL,
    item_name		VARCHAR(20) NOT NULL,
    price			DECIMAL(10,2) DEFAULT(0),
    qtys			INT DEFAULT(1),
    discount		DECIMAL DEFAULT(0.05),
    bill_amount 	DECIMAL(10,2) GENERATED ALWAYS AS ((price-(price*discount))*qtys)
);
INSERT INTO product(id, date, item_name, price, qtys)
VALUES(1, '2023-10-25', 'BALL', 20.00, 15),(2, '2023-09-25', 'BAT', 1000.00, 4),(3, '2023-10-26', 'STUMPS', 300.00, 3),(4, '2023-10-15', 'RACKET', 1000.00, 4),(5, '2023-09-12', 'SHUTTLE', 20.00, 20);
INSERT INTO product(id, date, item_name, price)
VALUES(6, '2023-06-10', 'SALT', 100.00),(7, '2023-07-20', 'BOTTLE', 50.00);
SELECT * FROM product WHERE bill_amount BETWEEN 600 AND 1200;
SELECT * FROM product WHERE qtys > 10;
SELECT * FROM product WHERE item_name LIKE 'S%';
SELECT * FROM product WHERE price < 1000 AND qtys > 5;
SELECT SUM(price) FROM product;
SELECT MIN(date) FROM product;
SELECT MAX(bill_amount - (discount * qtys)) FROM product;
SELECT MIN(bill_amount - (discount * qtys)) FROM product;
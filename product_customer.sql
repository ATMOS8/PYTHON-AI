CREATE TABLE product(
	id			INT PRIMARY KEY,
    prodname	VARCHAR(50) NOT NULL
);
CREATE TABLE customer(
	id 				INT PRIMARY KEY,
    customer_name	VARCHAR(50) NOT NULL
);
CREATE TABLE productcustomer(
	id 				INT PRIMARY KEY,
    fkcustomer		INT NOT NULL,
    fkproduct		INT NOT NULL,
    price			INT NOT NULL,
    qty				INT NOT NULL,
    total			DECIMAL(10,2) GENERATED ALWAYS AS (price * qty),
    FOREIGN KEY(fkcustomer) REFERENCES customer(id),
    FOREIGN KEY(fkproduct) REFERENCES product(id)
);
INSERT INTO product(id, prodname)
VALUES(1, "Speaker"), (2, "Mouse"), (3, "Keyboard"), (4, "Ram"), (5, "Processor"), (6, "Hard Disk");
INSERT INTO customer(id, customer_name)
VALUES(11, "Smith"), (12, "John"), (13, "Peter"), (14, "John");
INSERT INTO productcustomer(id, fkcustomer, fkproduct, price, qty)
VALUES(1, 11, 1, 600, 5), (2, 13, 1, 700, 3), (3, 13, 2, 1000, 9), (4, 12, 4, 2400, 2), (5, 11, 3, 3600, 1), (6, 14, 1, 2100, 7), (7, 12, 2, 500, 9);
SELECT * FROM customer;
SELECT * FROM  product;
SELECT * FROM productcustomer;
SELECT C.customer_name,P.prodname,PC.qty
FROM productcustomer PC
JOIN customer C ON PC.fkcustomer=C.id
JOIN product P ON PC.fkproduct=P.id;
SELECT P.prodname,COUNT(PC.fkcustomer)
FROM productcustomer PC
JOIN product P ON PC.fkproduct=P.id
GROUP BY P.prodname;
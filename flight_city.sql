CREATE TABLE city(
	id 		INT PRIMARY KEY,
    city 	VARCHAR(100) UNIQUE
);
CREATE TABLE flight(
	id 				INT PRIMARY KEY,
    flight_name 	VARCHAR(100) UNIQUE,
    airport_id 		INT NOT NULL,
    FOREIGN KEY(airport_id) REFERENCES city(id)
);
INSERT INTO city(id, city) 
VALUES(1, "NEW YORK"), (2, "WASHINGTON DC"), (3, "LOS ANGELES"), (4, "SAN FRANCISCO"), (5, "CHICAGO");
INSERT INTO flight(id, flight_name, airport_id)
VALUES(1, "AMERICAN AIRLINES", 1), (2, "VIRGIN AIRWAYS", 2), (3, "FLY EMIRATS", 3), (4, "ETIHAD AIRWAYS", 4);
SELECT * FROM city;
SELECT * FROM flight;
SELECT F1.id,C1.city,F1.flight_name
FROM flight F1
JOIN city C1 ON F1.airport_id=C1.id;
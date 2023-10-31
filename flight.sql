CREATE TABLE flight (
	id 				INT PRIMARY KEY,
    journey_date	DATE NOT NULL,
    flight_name 	CHAR(50) NOT NULL,
    passengers 		INT DEFAULT(50),
    ticket_cost		DECIMAL(20,2) DEFAULT(5000.00),
    departure_time	DATETIME NOT NULL
);

INSERT INTO flight VALUES(1, '2023/10/25', 'VISTARA', 50, 15000.00, '2023-10-25 15:15:15');

INSERT INTO flight(id, journey_date, flight_name, departure_time)
VALUES(2, '2023/10/26', 'AIR INDIA', '2023-10-26 10:10:00'), (3, '2023/10/27', 'INDIGO', '2023-10-27 10:11:00'), (4, '2023/10/28', 'AIR ASIA', '2023-10-28 00:12:00');

SELECT * FROM flight;

SELECT id, journey_date, flight_name FROM flight;
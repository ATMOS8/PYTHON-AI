CREATE TABLE movie(
	id				INT PRIMARY KEY,
    movie_name		VARCHAR(100) NOT NULL,
    rating 			INT DEFAULT(1),
    date			DATETIME DEFAULT NOW(),
    ticket_cost 	DECIMAL(10,2) NOT NULL
);
INSERT INTO movie(id, movie_name, rating, date, ticket_cost)
VALUES(1, 'AVENGERS', 9, '2012-12-12', 500.00),(2, 'HULK', 6, '2008-10-10', 100.00),(3, 'CAPTAIN AMERICA', 7, '2012-10-15', 200.00),(4, 'IRON MAN', 8, '2010-12-12', 300.00),(5, 'THOR', 8, '2012-06-10', 400.00);
SELECT movie_name FROM movie WHERE movie_name LIKE '%A%' OR '%M%';
SELECT MIN(rating) FROM movie;
SELECT MAX(ticket_cost) FROM movie;
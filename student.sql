CREATE TABLE student(
	roll_no 		INT PRIMARY KEY,
    student_name	VARCHAR(60) NOT NULL,
    sub1			INT DEFAULT(40),
    sub2			INT NULL,
    total			INT NULL,
    percentage 		DECIMAL(10,2) NOT NULL
);

INSERT INTO student (roll_no, student_name, sub1, sub2, total, percentage)
VALUES(1, 'JAMES', 50, 60, 110, 55.00),(2, 'CHRISTOPHER', 60, 60, 120, 60.00);

INSERT INTO student (roll_no, student_name, sub2, total, percentage)
VALUES(3, 'JOHN', 50, 90, 45.00),(4, 'JACK', 60, 100, 50.00),(5, 'PHILL', 70, 110, 55.00),(6, 'JEFFERY', 80, 120, 60.00),(7, 'NICK', 90, 130, 65.00);

SELECT roll_no AS rollno, student_name AS studentname FROM student;

SELECT * FROM student;

SELECT roll_no, student_name, sub1, sub2, total AS addition, percentage AS perc FROM student; 
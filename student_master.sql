CREATE TABLE branch(
	id 			INT PRIMARY KEY,
    branchname	VARCHAR(100) UNIQUE
);
CREATE TABLE subject(
	id 				INT PRIMARY KEY,
    subject_name	VARCHAR(100),
    total_marks		 INT NOT NULL
);
CREATE TABLE student(
	id 				INT PRIMARY KEY,
    student_name	VARCHAR(100) NOT NULL,
    fkbranchid		INT NOT NULL,
    FOREIGN KEY(fkbranchid) REFERENCES branch(id)
);
CREATE TABLE student_master(
	id 			INT PRIMARY KEY,
    fkstudentid	INT NOT NULL,
    fksubjectid	INT NOT NULL,
    FOREIGN KEY(fkstudentid) REFERENCES student(id),
    FOREIGN KEY(fksubjectid) REFERENCES subject(id)
);
INSERT INTO branch(id, branchname)
VALUES (1, "COMPUTER SCIENCE"), (2, "INFORMATION TECHNOLOGY"), (3, "ELECTRONICS AND TELECOMMUNICATION");
INSERT INTO subject(id, subject_name, total_marks)
VALUES (1, "COMPUTER SYSTEMS", 100), (2, "DATABASE SYSTEMS", 100), (3, "SOFTWARE ENGINEERING", 120), (4, "COMPILER DESIGN", 120), (5, "EMBEDDED SYSTEMS", 80), (6, "MICROPROCESSORS AND MICROCONTROLLERS", 80);
INSERT INTO student(id, student_name, fkbranchid)
VALUES (1, "JOHN WALKER", 1), (2, "NICK FURY", 1), (3, "PHILL COULSON", 2), (4, "JEFFERY MACE", 2), (5, "ALPHANSO MACKENZIE", 3);
SELECT * FROM branch;
SELECT * FROM subject;
SELECT * FROM student;
INSERT INTO student_master(id, fkstudentid, fksubjectid)
VALUES(1, 1, 1), (2, 3, 2), (3, 5, 3);
SELECT S1.id,S2.student_name,S3.subject_name,S3.total_marks
FROM student_master S1
JOIN student S2 ON S1.fkstudentid=S2.id
JOIN subject S3 ON S1.fksubjectid=S3.id;
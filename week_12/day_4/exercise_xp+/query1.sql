-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

CREATE TABLE students(
 student_id SERIAL PRIMARY KEY,
 student_lastname VARCHAR (100) NOT NULL,
 student_firstname VARCHAR (100) NOT NULL,
 student_birthdate DATE NOT NULL
)
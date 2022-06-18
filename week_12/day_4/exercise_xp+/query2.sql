INSERT INTO public.students(
	student_lastname, student_firstname, student_birthdate)
	VALUES
	('Benichou', 'Marc','1998-11-02'), 
	('Cohen', 'Yoan','2010-12-03'),
	('Benichou', 'Lea', '1987-07-27'),
	('Dux', 'Amelia', '1996-04-07'),
	('Grez', 'David', '2003-06-14'),
	('Simpson', 'Omer', '1980-10-03');


SELECT *
	FROM public.students;

-- To delete duplicates created by running several times this query
DELETE FROM public.students
    WHERE student_id NOT IN
    (
        SELECT MIN(student_id) AS MinRecordID
        FROM public.students
        GROUP BY student_lastname, 
                 student_firstname, 
                 student_birthdate
    );


SELECT *
	FROM public.students;


SELECT student_firstname, student_lastname
	FROM public.students;
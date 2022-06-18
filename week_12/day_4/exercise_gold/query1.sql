SELECT student_firstname, student_lastname, student_birthdate
	FROM public.students
	WHERE student_id<5
	ORDER BY student_lastname ASC;
	
--

SELECT student_firstname, student_lastname, student_birthdate
	FROM public.students
	ORDER BY student_birthdate DESC
	LIMIT 1;
	
--

SELECT student_firstname, student_lastname, student_birthdate
	FROM public.students
	ORDER BY student_birthdate DESC
	LIMIT 1;
	
--

SELECT student_firstname, student_lastname, student_birthdate
	FROM public.students
	LIMIT 3 OFFSET 2;
 

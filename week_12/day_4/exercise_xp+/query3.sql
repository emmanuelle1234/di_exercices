SELECT student_firstname, student_lastname
	FROM public.students;
	
--

SELECT student_firstname, student_lastname
	FROM public.students
	WHERE student_id=2;
	
--

SELECT student_firstname, student_lastname
	FROM public.students
	WHERE student_lastname='Benichou' AND student_firstname='Marc';
	
--

SELECT student_firstname, student_lastname
	FROM public.students
	WHERE student_lastname='Benichou' OR student_firstname='Marc';

--

SELECT student_firstname, student_lastname
	FROM public.students
	WHERE student_firstname ILIKE '%a%';
	
--

SELECT student_firstname, student_lastname
	FROM public.students
	WHERE student_firstname ILIKE 'a%';
	
--

SELECT student_firstname, student_lastname
	FROM public.students
	WHERE student_firstname ILIKE '%a';
	
--

SELECT student_firstname, student_lastname
	FROM public.students
	WHERE student_firstname ILIKE '%a%' AND SUBSTRING(student_firstname, 1, 1) NOT ILIKE 'a';
	
--

SELECT student_firstname, student_lastname
	FROM public.students
	WHERE student_id IN (1, 3);
	
--

SELECT *
	FROM public.students
	WHERE student_birthdate > '2000-01-01';
		
	
	
	
INSERT INTO public.actors(
	first_name, last_name, age, number_oscars)
	VALUES ('Ronit', 'Elkabets', '1900-01-01', 0);
	
---ERROR if blank fields
---ERROR if NULL : violation of constraint
---Constraints can be removed on actors > property and default value can be set there 
---or at creation of the table : age DEFAULT 'default_value'
---0 is not a good default value for number_oscars
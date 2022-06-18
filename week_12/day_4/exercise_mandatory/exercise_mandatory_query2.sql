-- CHANGE DATATYPE MONEY
-- 1. MONEY TO NUMERIC IN COLUMN PROPERTIES
-- 2. QUERY BELOW
-- "ALTER TABLE public.items 
-- ALTER COLUMN item_price SET DATA TYPE float"
-- Conclusion : avoid MONEY datatype

SELECT *
	FROM public.items
	WHERE item_price> 80


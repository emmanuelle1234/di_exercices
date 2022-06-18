-- 1. GUESS BEFORE : 3
-- ( SELECT id FROM SecondTab WHERE id IS NULL ) : 2nd record where id is NULL
-- Count the id in the first table where id is not NULL, so 3
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );
-- CHECK : 0
-- Don't understand. Even if we say ( SELECT id FROM SecondTab WHERE id IS NULL ) = UNKNOWN,
-- all id of the first table are known so it should be 4
-- Perhaps cannot select when is is NULL so NOT IN = NOT IN(everything) = NOT anyone ??


-- 2. GUESS BEFORE : 2
-- Not 5 (second table) and ignore null (first table)
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );
-- CHECK : 2


-- 3. GUESS BEFORE : 2
-- Not 5 (second table) and not null (first table)
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab );
-- CHECK : 0
-- Don't understand as SELECT id FROM SecondTab gives 5 and NULL


-- 4. GUESS BEFORE : 2
-- Not 5 (second table) and not null (first table)
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL );
-- CHECK : 2


SELECT DISTINCT(city)
FROM station
WHERE LEFT(LOWER(city), 1) NOT IN ('a', 'e', 'i', 'u', 'o') 
AND RIGHT(city, 1) NOT IN ('a', 'e', 'i', 'u', 'o') ;
SELECT DISTINCT(city)
FROM station
WHERE LEFT(LOWER(city), 1) IN ('a', 'e', 'i', 'o', 'u') 
AND RIGHT(city, 1) IN ('a', 'e', 'i', 'o', 'u');
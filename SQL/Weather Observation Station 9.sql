SELECT DISTINCT(city)
FROM station
WHERE LEFT(LOWER(city), 1) NOT IN ('a', 'i', 'u', 'e', 'o');

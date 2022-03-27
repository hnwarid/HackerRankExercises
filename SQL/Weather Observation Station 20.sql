SET @row_index := -1;

SELECT ROUND(AVG(subq.lat_n), 4) AS median
FROM (
        SELECT @row_index:= @row_index + 1 AS row_index, lat_n 
        FROM station
        ORDER BY lat_n
    ) AS subq
    WHERE subq.row_index
    IN (FLOOR(@row_index / 2), CEIL(@row_index / 2))
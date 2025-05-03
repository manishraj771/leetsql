SELECT 
    MAX(num) AS num
FROM (
    SELECT 
        num
    FROM 
        MyNumbers
    GROUP BY 
        num
    HAVING 
        COUNT(*) = 1
) AS SingleNumbers;
-- The subquery selects numbers that appear exactly once (COUNT(*) = 1)
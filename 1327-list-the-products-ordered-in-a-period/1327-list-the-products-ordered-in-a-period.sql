SELECT 
    p.product_name,
    SUM(O.unit) AS unit
FROM 
    Products p
JOIN 
    Orders O
ON 
    p.product_id = O.product_id
WHERE 
    MONTH(O.order_date) = 2 AND YEAR(O.order_date) = 2020
GROUP BY 
    p.product_name
HAVING 
    SUM(O.unit) >= 100;
# having used for condition here
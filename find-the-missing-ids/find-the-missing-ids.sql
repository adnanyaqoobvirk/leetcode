WITH RECURSIVE AllIds AS (
    SELECT 1 as ids
    
    UNION ALL
    
    SELECT ids + 1 FROM AllIds WHERE ids < (SELECT max(customer_id) FROM Customers)
)

SELECT
    A.ids
FROM
    AllIds AS A
    LEFT JOIN
    Customers AS C
    ON
        A.ids = C.customer_id
WHERE
    C.customer_id IS NULL
ORDER BY
    A.ids ASC
    

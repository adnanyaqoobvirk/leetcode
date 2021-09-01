WITH RECURSIVE AllIds AS (
    SELECT 
        1 as ids
    
    UNION ALL
    
    SELECT 
        ids + 1 
    FROM 
        AllIds
    WHERE 
        ids < (
            SELECT 
                max(customer_id) 
            FROM 
                Customers
        )
)

SELECT
    ids
FROM
    AllIds
WHERE
    ids NOT IN (
        SELECT
            customer_id
        FROM
            Customers
    )
ORDER BY
    ids ASC

WITH LatestProductSales AS (
    SELECT
        product_id,
        order_id,
        order_date,
        RANK() OVER(
            PARTITION BY product_id
            ORDER BY order_date DESC
        ) AS drank
    FROM
        Orders
)

SELECT
    P.product_name,
    L.product_id,
    L.order_id,
    L.order_date
FROM
    LatestProductSales AS L
    INNER JOIN
    Products AS P
    ON 
        L.drank = 1 
        AND 
        L.product_id = P.product_id
ORDER BY
    P.product_name,
    P.product_id,
    L.order_id
WITH ProductSales AS (
    SELECT
        P.product_id,
        S.year,
        S.quantity,
        S.price,
        RANK() OVER(
            PARTITION BY P.product_id
            ORDER BY S.year ASC
        ) AS prank
    FROM
        Product AS P
        INNER JOIN
        Sales AS S
        ON
            P.product_id = S.product_id
)

SELECT
    product_id,
    year as first_year,
    quantity,
    price
FROM
    ProductSales
WHERE
    prank = 1
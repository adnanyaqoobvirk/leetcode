SELECT
    ROUND(
        AVG(D.order_date = D.customer_pref_delivery_date) * 100,
        2
    ) AS immediate_percentage
FROM
    (
        SELECT
            customer_id,
            MIN(order_date) AS first_order_date
        FROM
            Delivery
        GROUP BY
            customer_id
    ) AS F
    INNER JOIN
    Delivery AS D
    ON
        F.customer_id = D.customer_id
        AND
        F.first_order_date = D.order_date

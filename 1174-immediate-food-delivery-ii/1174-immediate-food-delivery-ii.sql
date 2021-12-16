SELECT
    ROUND(
        AVG(D.order_date = D.customer_pref_delivery_date) * 100,
        2
    ) AS immediate_percentage
FROM
    (
        SELECT
            order_date,
            customer_pref_delivery_date,
            RANK() OVER(
                PARTITION BY customer_id
                ORDER BY order_date ASC
            ) AS orank
        FROM
            Delivery
    ) AS D
WHERE
    D.orank = 1
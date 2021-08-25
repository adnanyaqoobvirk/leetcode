SELECT
    S.user_id,
    IF(
        COUNT(C.action) = 0, 
        0.00,
        ROUND(
            SUM(C.action = 'confirmed') / COUNT(C.action),
            2
        )
    ) AS confirmation_rate
FROM
    Signups AS S
    LEFT JOIN
    Confirmations AS C
    ON
        S.user_id = C.user_id
GROUP BY
    S.user_id
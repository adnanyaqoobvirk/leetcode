SELECT
    S.user_id,
    ROUND(
        AVG(IF(C.action = 'confirmed', 1, 0)),
        2
    ) AS confirmation_rate
FROM
    Signups AS S
    LEFT JOIN
    Confirmations AS C
    ON
        S.user_id = C.user_id
GROUP BY
    S.user_id
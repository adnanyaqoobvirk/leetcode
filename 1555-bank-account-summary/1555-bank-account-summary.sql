SELECT
    U.user_id,
    U.user_name,
    credit + IFNULL(
        SUM(
            IF(
                T.paid_by = U.user_id,
                -T.amount, 
                T.amount
            )
        ),
        0
    )AS credit,
    IF(
        credit + IFNULL(
            SUM(
                IF(
                    T.paid_by = U.user_id,
                    -T.amount, 
                    T.amount
                )
            ),
            0
        ) < 0, 
        'Yes', 
        'No'
    ) AS credit_limit_breached
FROM
    Users AS U
    LEFT JOIN
    Transactions AS T
    ON
        U.user_id = T.paid_by 
        OR 
        U.user_id = T.paid_to
GROUP BY
    U.user_id
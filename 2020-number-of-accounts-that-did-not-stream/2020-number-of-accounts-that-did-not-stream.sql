SELECT
    COUNT(S.account_id) AS accounts_count
FROM
    (
        SELECT
            DISTINCT account_id
        FROM
            Subscriptions
        WHERE
            YEAR(start_date) = 2021 OR YEAR(end_date) = 2021
    ) AS S
    LEFT JOIN
    (
        SELECT
            DISTINCT account_id
        FROM
            Streams
        WHERE
            YEAR(stream_date) = 2021
    ) AS ST
    ON
        S.account_id = ST.account_id
WHERE
    ST.account_id IS NULL
    

SELECT
    COUNT(account_id) AS accounts_count
FROM
    Subscriptions
WHERE
    YEAR(end_date) = 2021
    AND
    account_id NOT IN (
        SELECT
            account_id
        FROM
            Streams
        WHERE
            YEAR(stream_date) = 2021
    )

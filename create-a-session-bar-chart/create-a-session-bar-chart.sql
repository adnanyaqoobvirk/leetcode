WITH SessionsInMinutes AS (
    SELECT
        duration / 60 AS duration_minutes
    FROM
        Sessions
), Bins AS (
    SELECT
        CASE
            WHEN duration_minutes < 5 THEN '[0-5>'
            WHEN duration_minutes < 10 AND duration_minutes >= 5 THEN '[5-10>'
            WHEN duration_minutes < 15 AND duration_minutes >= 10 THEN '[10-15>'
            ELSE '15 or more'
        END AS bin
    FROM
        SessionsInMinutes
)

SELECT
    T.bin,
    COUNT(B.bin) AS total
FROM
    (
        SELECT '[0-5>' AS bin
        UNION ALL
        SELECT '[5-10>' AS bin
        UNION ALL
        SELECT '[10-15>' AS bin
        UNION ALL
        SELECT '15 or more' AS bin
    ) AS T
    LEFT JOIN
    Bins AS B
    ON
        T.bin = B.bin
GROUP BY
    T.bin

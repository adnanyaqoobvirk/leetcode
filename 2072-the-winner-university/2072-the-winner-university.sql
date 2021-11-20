WITH UCounts AS (
    SELECT
    (
        SELECT
            COUNT(*) AS students
        FROM
            NewYork
        WHERE
            score >= 90
    ) AS NY,
    (
        SELECT
            COUNT(*) AS students
        FROM
            California
        WHERE
            score >= 90
    ) AS CA
)

SELECT
    CASE
        WHEN
            NY > CA
        THEN
            'New York University'
        WHEN
            CA > NY
        THEN
            'California University'
        ELSE
            'No Winner'
    END AS winner
FROM
    UCounts
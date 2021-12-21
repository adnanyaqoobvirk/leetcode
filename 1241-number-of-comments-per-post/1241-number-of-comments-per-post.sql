WITH T AS (
    SELECT
        parent_id,
        COUNT(DISTINCT sub_id) AS ncoments
    FROM
        Submissions
    WHERE
        parent_id IS NOT NULL
    GROUP BY
        parent_id
), S AS (
    SELECT
        DISTINCT sub_id
    FROM
        Submissions
    WHERE
        parent_id IS NULL
)

SELECT
    S.sub_id AS post_id,
    IF(T.ncoments IS NULL, 0, T.ncoments) AS number_of_comments
FROM
    S LEFT JOIN T ON S.sub_id = T.parent_id
ORDER BY
    post_id

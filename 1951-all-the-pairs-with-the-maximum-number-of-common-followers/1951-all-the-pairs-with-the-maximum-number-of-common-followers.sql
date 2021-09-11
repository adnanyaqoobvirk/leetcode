WITH CommonFollowers AS (
    SELECT
        R1.user_id AS user1_id,
        R2.user_id AS user2_id,
        DENSE_RANK() OVER(
            ORDER BY COUNT(R2.user_id) DESC
        ) AS frank
    FROM
        Relations AS R1
        INNER JOIN
        Relations AS R2
        ON
            R2.user_id > R1.user_id
            AND
            R1.follower_id = R2.follower_id
    GROUP BY
        R1.user_id,
        R2.user_id
)

SELECT
    user1_id,
    user2_id
FROM
    CommonFollowers
WHERE
    frank = 1
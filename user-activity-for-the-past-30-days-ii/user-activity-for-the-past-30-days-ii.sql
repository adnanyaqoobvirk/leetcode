SELECT
    ROUND(
        IFNULL(
            AVG(session_count), 
            0.0
        ), 
        2
    ) AS average_sessions_per_user
FROM
    (
        SELECT
            COUNT(DISTINCT session_id) AS session_count
        FROM
            Activity
        WHERE
            activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
        GROUP BY
            user_id
    ) AS T

WITH UserFirstLogins AS (
    SELECT
        user_id,
        MIN(activity_date) AS login_date
    FROM
        Traffic
    WHERE
        activity = 'login'
    GROUP BY
        user_id
    HAVING
        login_date >= '2019-06-30' - INTERVAL 90 DAY
)

SELECT
    login_date,
    COUNT(user_id) AS user_count
FROM
    UserFirstLogins
GROUP BY
    login_date
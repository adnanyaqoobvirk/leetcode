SELECT
    CASE
        WHEN
            (
                SELECT
                    COUNT(*) AS students
                FROM
                    NewYork
                WHERE
                    score >= 90
            )
            >
            (
                SELECT
                    COUNT(*) AS students
                FROM
                    California
                WHERE
                    score >= 90
            )
        THEN
            'New York University'
        WHEN
            (
                SELECT
                    COUNT(*) AS students
                FROM
                    NewYork
                WHERE
                    score >= 90
            )
            <
            (
                SELECT
                    COUNT(*) AS students
                FROM
                    California
                WHERE
                    score >= 90
            )
        THEN
            'California University'
        ELSE
            'No Winner'
    END AS winner
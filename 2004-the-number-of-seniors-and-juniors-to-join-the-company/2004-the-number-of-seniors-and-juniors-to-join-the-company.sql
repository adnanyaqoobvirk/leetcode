WITH SelectedSeniors AS (
    SELECT
        salary
    FROM
    (
        SELECT
            experience,
            salary,
            SUM(salary) OVER(ORDER BY salary ASC) AS run_sum
        FROM
            Candidates
        WHERE
            experience = 'Senior'
    ) AS T
    WHERE
        run_sum <= 70000
), SelectedJuniors AS (
    SELECT
        COUNT(run_sum) AS counts
    FROM
    (
        SELECT
            SUM(salary) OVER(ORDER BY salary ASC) AS run_sum
        FROM
            Candidates
        WHERE
            experience = 'Junior'
    ) AS T
    WHERE
        run_sum <= (
            70000 - (
                SELECT
                    IFNULL(SUM(salary), 0)
                FROM
                    SelectedSeniors
            )
        )
)

SELECT
    'Senior' AS experience,
    COUNT(*) AS accepted_candidates
FROM
    SelectedSeniors

UNION ALL

SELECT
    'Junior' AS experience,
    counts AS accepted_candidates
FROM
    SelectedJuniors
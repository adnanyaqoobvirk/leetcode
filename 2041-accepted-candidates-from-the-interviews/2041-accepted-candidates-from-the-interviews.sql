SELECT
    C.candidate_id
FROM
    Candidates AS C
    INNER JOIN
    Rounds AS R
    ON
        C.interview_id = R.interview_id
        AND
        C.years_of_exp > 1
GROUP BY
    C.candidate_id
HAVING
    SUM(R.score) > 15
SELECT
    S.school_id,
    MIN(IFNULL(E.score, -1)) AS score
FROM
    Schools AS S
    LEFT JOIN
    Exam AS E
    ON
        E.student_count <= S.capacity
GROUP BY
    S.school_id

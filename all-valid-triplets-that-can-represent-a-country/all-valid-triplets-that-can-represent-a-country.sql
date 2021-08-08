SELECT
    A.student_name AS member_A,
    B.student_name AS member_B,
    C.student_name AS member_C
FROM
    SchoolA AS A
    INNER JOIN
    SchoolB AS B
    ON
        A.student_id != B.student_id
        AND
        A.student_name != B.student_name
    INNER JOIN
    SchoolC AS C
    ON
        A.student_id != C.student_id
        AND
        A.student_name != C.student_name
        AND
        B.student_id != C.student_id
        AND
        B.student_name != C.student_name

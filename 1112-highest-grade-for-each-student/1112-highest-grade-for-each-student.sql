select
    student_id,
    course_id,
    grade
from
    (
        select
            student_id,
            course_id,
            grade,
            rank() over(
                partition by student_id
                order by grade desc, course_id asc
            ) as crank
        from
            Enrollments
    ) as t
where
    crank = 1
order by
    student_id

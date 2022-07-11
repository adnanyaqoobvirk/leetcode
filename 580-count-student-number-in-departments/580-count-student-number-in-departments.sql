select
    d.dept_name,
    sum(if(s.student_id is null, 0, 1)) as student_number
from
    Department as d
    left join
    Student as s
    on
        d.dept_id = s.dept_id
group by
    d.dept_id
order by
    student_number desc,
    d.dept_name asc
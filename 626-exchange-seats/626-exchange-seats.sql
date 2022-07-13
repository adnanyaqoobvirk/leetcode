select
    id,
    ifnull(
        if((id % 2) = 0, lag(student) over(), lead(student) over()),
        student
    ) as student
from
    seat
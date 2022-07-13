select
    seat_id
from
    (
        select
            seat_id,
            if(
                free = 1 
                and 
                (lag(free) over() = 1 or lead(free) over() = 1),
                1, 
                0
            ) as include
        from
            Cinema
    ) as t
where
    include = 1
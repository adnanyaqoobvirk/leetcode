select
    p1.id as p1,
    p2.id as p2,
    abs(p1.x_value - p2.x_value) * abs(p1.y_value - p2.y_value) as area
from
    Points p1
    inner join 
    Points p2 
    on 
        p1.id < p2.id
having
    area > 0
order by
    area desc,
    p1 asc,
    p2 asc
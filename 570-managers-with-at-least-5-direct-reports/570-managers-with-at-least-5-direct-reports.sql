select
    e.name
from
    (
        select
            managerId
        from
            Employee
        where
            managerId is not null
        group by
            managerId
        having
            count(id) >= 5
    ) as t
    inner join
    Employee as e
    on
        e.id = t.managerId
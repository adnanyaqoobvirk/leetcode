select
    Department,
    Employee,
    Salary
from
    (
        select
            d.name as Department,
            e.name as Employee,
            e.salary as Salary,
            rank() over(
                partition by d.name
                order by e.salary desc
            ) as srank
        from
            Department as d
            inner join
            Employee as e
            on
                d.id = e.departmentId
    ) as t
where
    srank = 1
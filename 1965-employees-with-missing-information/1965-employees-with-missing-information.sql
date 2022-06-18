select
    t.employee_id
from
    (
        select
            e.employee_id,
            e.name,
            s.salary
        from
            Employees e
            left join
            Salaries s
            on
                e.employee_id = s.employee_id
        
        UNION
        
        select
            s.employee_id,
            e.name,
            s.salary
        from
            Employees e
            right join
            Salaries s
            on
                e.employee_id = s.employee_id
    ) t
where
    t.name is null or t.salary is null
order by
    t.employee_id
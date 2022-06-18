select
    salary as SecondHighestSalary
from
    (
        select
            distinct
            salary
        from    
            Employee
        
        union all
        
        select null
    ) t
order by
    salary desc
limit 1, 1

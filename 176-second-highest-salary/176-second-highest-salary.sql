select
    salary as SecondHighestSalary
from
    (
        select
            salary,
            dense_rank() over(order by salary desc) srank
        from    
            Employee
        
        union all
        
        select 
            null,
            2
    ) t
where
    t.srank = 2
order by
    t.salary desc
limit 1
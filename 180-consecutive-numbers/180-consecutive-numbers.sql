select
    distinct num as ConsecutiveNums
from
    (
        select
            num,
            if(
                lag(num, 1) over() = num 
                and
                lag(num, 2) over() = num,
                1,
                0
            ) as include
        from
            Logs
    ) as t
where
    t.include = 1
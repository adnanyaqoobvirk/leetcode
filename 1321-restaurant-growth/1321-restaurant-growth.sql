select
    distinct
    visited_on,
    amount,
    round(amount / 7, 2) as average_amount
from
    (
        select
            visited_on,
            sum(amount) over(
                order by visited_on asc
                range between interval 6 day preceding and current row
            ) as amount,
            dense_rank() over(
                order by visited_on asc
            ) as drank
        from
            Customer
    ) as t
where
    drank >= 7
order by
    visited_on asc
    
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
            ) as amount
        from
            Customer
    ) as t
order by
    visited_on
limit 
    18446744073709551615
offset 
    6
    
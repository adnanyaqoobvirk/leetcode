select
    customer_number
from
(
    select
        customer_number,
        rank() over(
            order by count(order_number) desc
        ) as orank
    from
        Orders
    group by
        customer_number
) t
where
    t.orank = 1

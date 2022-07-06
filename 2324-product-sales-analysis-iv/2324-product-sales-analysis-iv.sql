select
    user_id,
    product_id
from
    (
        select
            s.user_id,
            p.product_id,
            rank() over(
                partition by s.user_id
                order by sum(s.quantity * p.price) desc
            ) as prank
        from
            Sales as s
            inner join
            Product as p
            on
                s.product_id = p.product_id
        group by
            s.user_id,
            p.product_id
    ) as t
where
    prank = 1

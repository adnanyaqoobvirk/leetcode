select
    p.product_id,
    ifnull(t.new_price, 10) as price
from
    (
        select
            distinct product_id
        from
            Products
    ) as p
    left join
    (
        select
            product_id,
            new_price,
            rank() over(
                partition by product_id
                order by change_date desc
            ) as drank
        from
            Products
        where
            change_date <= '2019-08-16'
    ) as t
    on
        p.product_id = t.product_id
        and
        t.drank = 1

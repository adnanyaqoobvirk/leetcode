select
    s.user_id,
    sum(s.quantity * p.price) as spending
from
    Sales as s
    inner join
    Product as p
    on
        s.product_id = p.product_id
group by
    s.user_id
order by
    spending desc,
    s.user_id asc
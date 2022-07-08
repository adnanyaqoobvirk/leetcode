select
    distinct seller_name
from
    Seller as s
    left join
    Orders as o
    on
        s.seller_id = o.seller_id
        and
        year(o.sale_date) = 2020
where
    o.seller_id is null
order by
    seller_name
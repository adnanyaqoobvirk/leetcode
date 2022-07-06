select
    w.name as warehouse_name,
    sum(p.Width * p.Length * p.Height * w.units) as volume
from
    Warehouse as w
    inner join
    Products as p
    on
        w.product_id = p.product_id
group by
    w.name

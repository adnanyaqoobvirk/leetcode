with LatestProductSales as (
    select
        product_id,
        order_id,
        order_date,
        rank() over(
            partition by product_id
            order by order_date desc
        ) as drank
    from
        Orders
)

select
    p.product_name,
    l.product_id,
    l.order_id,
    l.order_date
from
    LatestProductSales as l
    inner join
    Products as p
    on 
        l.drank = 1 
        and 
        l.product_id = p.product_id
order by
    p.product_name,
    p.product_id,
    l.order_id
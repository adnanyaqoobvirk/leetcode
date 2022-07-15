select
    order_id
from
    OrdersDetails
group by
    order_id
having
    max(quantity) > (
        select
            max(avg_quantity)
        from
        (
            select
                sum(quantity) / count(distinct product_id) as avg_quantity
            from
                OrdersDetails
            group by
                order_id
        ) as t
    )

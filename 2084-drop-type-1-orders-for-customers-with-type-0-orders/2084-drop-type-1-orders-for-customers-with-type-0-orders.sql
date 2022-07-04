select
    *
from
    Orders
where
    customer_id not in (
        select
            customer_id
        from
            Orders
        where
            order_type = 0
    )

union all

select
    *
from
    Orders
where
    customer_id in (
        select
            customer_id
        from
            Orders
        where
            order_type = 0
    )
    and
    order_type != 1
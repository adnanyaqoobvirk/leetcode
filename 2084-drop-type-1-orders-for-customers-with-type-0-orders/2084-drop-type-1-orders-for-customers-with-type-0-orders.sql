select
    *
from
    Orders
where
    not (
        order_type = 1 
        and 
        customer_id in (
            select
                customer_id
            from
                Orders
            where
                order_type = 0
        )
    )
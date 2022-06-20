select
    *
from
(
    select
        customer_id,
        count(customer_id) as count_no_trans
    from
        Visits v
        left join
        Transactions tr
        on
            v.visit_id = tr.visit_id
    where
        amount is null
    group by
        customer_id
) t
where
    t.count_no_trans > 0
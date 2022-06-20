select
    *
from
(
    select
        customer_id,
        sum(if(amount is null, 1, 0)) as count_no_trans
    from
        Visits v
        left join
        Transactions tr
        on
            v.visit_id = tr.visit_id
    group by
        customer_id
) t
where
    t.count_no_trans > 0
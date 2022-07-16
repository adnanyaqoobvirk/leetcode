select
    t.request_at as Day,
    round(
        sum(if(t.status != 'completed', 1, 0)) / count(id),
        2
    ) as `Cancellation Rate`
from
    Trips as t
    inner join
    Users as u1
    on
        t.request_at between '2013-10-01' and '2013-10-03'
        and
        t.client_id = u1.users_id
        and
        u1.banned = 'No'
    inner join
    Users as u2
    on
        t.driver_id = u2.users_id
        and
        u2.banned = 'No'
group by
    t.request_at
select
    c.name as country
from
    Country as c
    inner join
    (
        select
            substr(p.phone_number, 1, 3) as country_code,
            avg(ca.duration) as avg_duration
        from
            Calls as ca
            inner join
            Person as p
            on
                ca.caller_id = p.id
                or
                ca.callee_id = p.id
        group by
            country_code
    ) as t
    on
        c.country_code = t.country_code
where
    t.avg_duration > (
        select
            avg(duration)
        from
            Calls
    )
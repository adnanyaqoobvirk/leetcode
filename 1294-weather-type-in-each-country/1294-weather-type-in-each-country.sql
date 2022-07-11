select
    country_name,
    case
        when avg(weather_state) <= 15 then 'Cold'
        when avg(weather_state) >= 25 then 'Hot'
        else 'Warm'
    end as weather_type
from
    Countries as c
    inner join
    Weather as w
    on
        c.country_id = w.country_id
        and
        date_format(day, '%Y-%m') = '2019-11'
group by
    country_name
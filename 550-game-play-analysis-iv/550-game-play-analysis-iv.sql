select
    round(
        count(player_id) / (select count(distinct player_id) from Activity),
        2
    ) as fraction
from
    (
        select
            player_id,
            min(event_date) as begin_date
        from
            Activity
        group by
            player_id
    ) as t
where
    (player_id, begin_date + interval 1 day) in (
        select
            player_id,
            event_date
        from
            Activity
    )

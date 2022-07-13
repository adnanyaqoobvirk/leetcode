select
    p.player_id,
    p.player_name,
    sum(
        if(p.player_id = c.Wimbledon, 1, 0)
        +
        if(p.player_id = c.Fr_open, 1, 0)
        +
        if(p.player_id = c.US_open, 1, 0)
        +
        if(p.player_id = c.Au_open, 1, 0)
    ) as grand_slams_count
from
    Players as p
    inner join
    Championships as c
    on
        p.player_id in (
            c.Wimbledon,
            c.Fr_open,
            c.US_open,
            c.Au_open
        )
group by
    p.player_id

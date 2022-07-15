(
    select
        u.name as results
    from
        Users as u
        inner join
        MovieRating as m
        on
            u.user_id = m.user_id
    group by
        u.user_id
    order by
        count(m.movie_id) desc,
        u.name asc
    limit 
        1
)

union all

(
    select
        m.title as results
    from
        Movies as m
        inner join
        MovieRating as mr
        on
            m.movie_id = mr.movie_id
            and
            date_format(mr.created_at, '%Y-%m') = '2020-02'
    group by
        m.movie_id
    order by
        avg(mr.rating) desc,
        m.title asc
    limit 
        1
)
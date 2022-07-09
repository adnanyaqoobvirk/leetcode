select
    distinct page_id as recommended_page
from
    (
        select
            if(user1_id = 1, user2_id, user1_id) as user_id
        from
            Friendship
        where
            user1_id = 1 or user2_id = 1
    ) as t
    inner join
    likes as l
    on
        t.user_id = l.user_id
where
    page_id not in (
        select
            page_id
        from
            Likes
        where
            user_id = 1
    )

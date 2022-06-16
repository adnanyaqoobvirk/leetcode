delete from Person
where
    id not in
    (
        select
            min(p.id)
        from
            (select * from Person) p
        group by
            p.email
    )
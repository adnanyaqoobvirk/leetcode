select
    (
        select 
            count(submit_date) 
        from 
            Tasks 
        where 
            weekday(submit_date) >= 5
    ) as weekend_cnt,
    (
        select 
            count(submit_date) 
        from 
            Tasks 
        where 
            weekday(submit_date) < 5
    ) as working_cnt

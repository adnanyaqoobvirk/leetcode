select
    st.student_id,
    st.student_name,
    sb.subject_name,
    sum(if(e.subject_name is null, 0, 1)) as attended_exams
from
    Students as st
    join
    Subjects as sb
    left join
    Examinations as e
    on
        st.student_id = e.student_id
        and
        sb.subject_name = e.subject_name
group by
    st.student_id,
    st.student_name,
    sb.subject_name
order by
    student_id,
    subject_name
        
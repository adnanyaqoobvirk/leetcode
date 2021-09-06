WITH ActiveParticipants AS (
    SELECT
        A.name AS activity,
        Count(F.id) as participants
    FROM
        Activities AS A
        LEFT JOIN
        Friends AS F
        ON
            A.name = F.activity
    GROUP BY
        A.name
), MaxMinParticipants AS (
    SELECT
        MAX(participants) AS max_count,
        MIN(participants) AS min_count
    FROM
        ActiveParticipants
)

SELECT
    activity
FROM
    ActiveParticipants
WHERE
    participants NOT IN (
        SELECT 
            max_count
        FROM 
            MaxMinParticipants
        
        UNION ALL
        
        SELECT 
            min_count
        FROM 
            MaxMinParticipants
    )
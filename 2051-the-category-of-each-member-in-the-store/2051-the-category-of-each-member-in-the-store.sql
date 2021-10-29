SELECT
    M.member_id,
    M.name,
    CASE 
        WHEN COUNT(P.visit_id) / COUNT(V.visit_id) >= 0.8 THEN 'Diamond'
        WHEN COUNT(P.visit_id) / COUNT(V.visit_id) BETWEEN 0.5 and 0.8 THEN 'Gold'
        WHEN COUNT(P.visit_id) / COUNT(V.visit_id) < 0.5 THEN 'Silver'
        ELSE 'Bronze'
    END AS category
FROM
    Members AS M
    LEFT JOIN
    Visits AS V
    ON
        M.member_id = V.member_id
    LEFT JOIN
    Purchases AS P
    ON
        V.visit_id = P.visit_id
GROUP BY
    M.member_id

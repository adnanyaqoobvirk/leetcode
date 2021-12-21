SELECT
    P1.id AS p1,
    P2.id AS p2,
    ABS(p1.x_value - p2.x_value) * ABS(p1.y_value - p2.y_value) AS area
FROM
    Points P1
    INNER JOIN Points P2 ON P1.id < P2.id
HAVING
    area > 0
ORDER BY
    area DESC,
    p1 ASC,
    p2 ASC

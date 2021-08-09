WITH EmployeeIds AS (
    SELECT
        employee_id
    FROM
        Employees

    UNION ALL

    SELECT
        employee_id
    FROM
        Salaries
)

SELECT
    employee_id
FROM
    EmployeeIds
GROUP BY 
    employee_id
HAVING
    COUNT(*) = 1
ORDER BY
    employee_id ASC


-- HR Analytics & Employee Attrition Intelligence
-- SQL analysis queries
-- Database table: employees

-- 1. Overall employee attrition
SELECT
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        AS employees_left,
    SUM(CASE WHEN Attrition = 'No' THEN 1 ELSE 0 END)
        AS employees_stayed,
    ROUND(
        100.0 * SUM(
            CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct
FROM employees;


-- 2. Attrition by department
SELECT
    Department,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        AS employees_left,
    ROUND(
        100.0 * SUM(
            CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct
FROM employees
GROUP BY Department
ORDER BY attrition_rate_pct DESC;


-- 3. Attrition by job role
SELECT
    JobRole,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        AS employees_left,
    ROUND(
        100.0 * SUM(
            CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct
FROM employees
GROUP BY JobRole
ORDER BY attrition_rate_pct DESC;


-- 4. Attrition by overtime
SELECT
    OverTime,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        AS employees_left,
    ROUND(
        100.0 * SUM(
            CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct
FROM employees
GROUP BY OverTime
ORDER BY attrition_rate_pct DESC;


-- 5. Attrition by tenure group
SELECT
    CASE
        WHEN YearsAtCompany < 2 THEN '0-1 years'
        WHEN YearsAtCompany < 5 THEN '2-4 years'
        WHEN YearsAtCompany < 10 THEN '5-9 years'
        ELSE '10+ years'
    END AS tenure_group,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        AS employees_left,
    ROUND(
        100.0 * SUM(
            CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct
FROM employees
GROUP BY tenure_group
ORDER BY
    CASE tenure_group
        WHEN '0-1 years' THEN 1
        WHEN '2-4 years' THEN 2
        WHEN '5-9 years' THEN 3
        ELSE 4
    END;

    
-- 6. Check duplicate employee records
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT EmployeeNumber) AS unique_employee_numbers,
    COUNT(*) - COUNT(DISTINCT EmployeeNumber)
        AS duplicate_employee_numbers
FROM employees;


-- 7. Validate attrition categories
SELECT
    Attrition,
    COUNT(*) AS employee_count
FROM employees
GROUP BY Attrition
ORDER BY Attrition;


-- 8. Check for invalid employee values
SELECT
    SUM(CASE WHEN Age < 18 OR Age > 100 THEN 1 ELSE 0 END)
        AS invalid_age_count,
    SUM(CASE WHEN MonthlyIncome < 0 THEN 1 ELSE 0 END)
        AS invalid_income_count,
    SUM(CASE WHEN YearsAtCompany < 0 THEN 1 ELSE 0 END)
        AS invalid_tenure_count
FROM employees;


-- 9. Calculate attrition by tenure group
SELECT
    CASE
        WHEN YearsAtCompany < 2 THEN '0-1 years'
        WHEN YearsAtCompany < 5 THEN '2-4 years'
        WHEN YearsAtCompany < 10 THEN '5-9 years'
        ELSE '10+ years'
    END AS tenure_group,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        AS employees_left,
    ROUND(
        100.0 * SUM(
            CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS attrition_rate_pct
FROM employees
GROUP BY tenure_group
ORDER BY
    CASE tenure_group
        WHEN '0-1 years' THEN 1
        WHEN '2-4 years' THEN 2
        WHEN '5-9 years' THEN 3
        ELSE 4
    END;


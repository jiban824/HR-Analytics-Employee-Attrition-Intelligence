
from pathlib import Path
import sqlite3
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent

CSV_FILE = (
    PROJECT_DIR
    / "data"
    / "processed"
    / "hr_employee_attrition_cleaned.csv"
)

DB_DIR = PROJECT_DIR / "data" / "processed"
DB_FILE = DB_DIR / "hr_analytics.db"


def main():
    if not CSV_FILE.exists():
        raise FileNotFoundError(
            f"Cleaned CSV not found: {CSV_FILE}. "
            "Run src/clean_data.py first."
        )

    DB_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(CSV_FILE)

    with sqlite3.connect(DB_FILE) as connection:
        df.to_sql(
            "employees",
            connection,
            if_exists="replace",
            index=False
        )

        cursor = connection.cursor()

        # 1. Overall attrition
        print("\n1. OVERALL ATTRITION")
        query = """
        SELECT
            COUNT(*) AS total_employees,
            SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
                AS employees_left,
            ROUND(
                100.0 * SUM(
                    CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END
                ) / COUNT(*), 2
            ) AS attrition_rate_pct
        FROM employees;
        """
        print(pd.read_sql_query(query, connection).to_string(index=False))

        # 2. Attrition by department
        print("\n2. ATTRITION BY DEPARTMENT")
        query = """
        SELECT
            Department,
            COUNT(*) AS total_employees,
            SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
                AS employees_left,
            ROUND(
                100.0 * SUM(
                    CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END
                ) / COUNT(*), 2
            ) AS attrition_rate_pct
        FROM employees
        GROUP BY Department
        ORDER BY attrition_rate_pct DESC;
        """
        print(pd.read_sql_query(query, connection).to_string(index=False))

        # 3. Attrition by job role
        print("\n3. ATTRITION BY JOB ROLE")
        query = """
        SELECT
            JobRole,
            COUNT(*) AS total_employees,
            SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
                AS employees_left,
            ROUND(
                100.0 * SUM(
                    CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END
                ) / COUNT(*), 2
            ) AS attrition_rate_pct
        FROM employees
        GROUP BY JobRole
        ORDER BY attrition_rate_pct DESC;
        """
        print(pd.read_sql_query(query, connection).to_string(index=False))

        # 4. Overtime versus attrition
        print("\n4. ATTRITION BY OVERTIME")
        query = """
        SELECT
            OverTime,
            COUNT(*) AS total_employees,
            SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
                AS employees_left,
            ROUND(
                100.0 * SUM(
                    CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END
                ) / COUNT(*), 2
            ) AS attrition_rate_pct
        FROM employees
        GROUP BY OverTime
        ORDER BY attrition_rate_pct DESC;
        """
        print(pd.read_sql_query(query, connection).to_string(index=False))

        # 5. Attrition by tenure band
        print("\n5. ATTRITION BY YEARS AT COMPANY")
        query = """
        SELECT
            CASE
                WHEN YearsAtCompany < 2 THEN '0-1 years'
                WHEN YearsAtCompany < 5 THEN '2-4 years'
                WHEN YearsAtCompany < 10 THEN '5-9 years'
                ELSE '10+ years'
            END AS tenure_band,
            COUNT(*) AS total_employees,
            SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
                AS employees_left,
            ROUND(
                100.0 * SUM(
                    CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END
                ) / COUNT(*), 2
            ) AS attrition_rate_pct
        FROM employees
        GROUP BY tenure_band
        ORDER BY
            CASE tenure_band
                WHEN '0-1 years' THEN 1
                WHEN '2-4 years' THEN 2
                WHEN '5-9 years' THEN 3
                ELSE 4
            END;
        """
        print(pd.read_sql_query(query, connection).to_string(index=False))

    print(f"\nDatabase saved to: {DB_FILE}")


if __name__ == "__main__":
    main()

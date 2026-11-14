
from pathlib import Path
import sqlite3
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent

SQL_FILE = PROJECT_DIR / "sql" / "hr_attrition_analysis.sql"
DB_FILE = PROJECT_DIR / "data" / "processed" / "hr_analytics.db"


def main():
    if not SQL_FILE.exists():
        raise FileNotFoundError(f"SQL file not found: {SQL_FILE}")

    if not DB_FILE.exists():
        raise FileNotFoundError(
            f"Database not found: {DB_FILE}\n"
            "Run src/sql_analysis.py first."
        )

    sql_text = SQL_FILE.read_text(encoding="utf-8")
    statements = [
        statement.strip()
        for statement in sql_text.split(";")
        if statement.strip()
    ]

    with sqlite3.connect(DB_FILE) as connection:
        # Confirm that the employees table exists.
        tables = pd.read_sql_query(
            "SELECT name FROM sqlite_master WHERE type='table'",
            connection,
        )["name"].tolist()

        if "employees" not in tables:
            raise ValueError(
                "The employees table is missing. "
                "Run src/sql_analysis.py first."
            )

        for number, statement in enumerate(statements, start=1):
            cursor = connection.execute(statement)

            if cursor.description:
                columns = [item[0] for item in cursor.description]
                rows = cursor.fetchall()
                result = pd.DataFrame(rows, columns=columns)

                print(f"\n{'=' * 60}")
                print(f"SQL QUERY {number}")
                print("=" * 60)
                print(result.to_string(index=False))

    print("\nAll SQL queries executed successfully.")


if __name__ == "__main__":
    main()

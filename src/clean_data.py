
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    PROJECT_DIR / "data" / "raw"
    / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

OUTPUT_DIR = PROJECT_DIR / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "hr_employee_attrition_cleaned.csv"


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {INPUT_FILE}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load the original data without modifying it
    df = pd.read_csv(INPUT_FILE)

    original_rows = len(df)

    print("Starting data quality checks...")
    print(f"Original rows: {original_rows}")
    print(f"Original columns: {len(df.columns)}")

    # 1. Normalize column-name whitespace
    df.columns = df.columns.str.strip()

    # 2. Remove exact duplicate rows, if any
    duplicate_count = int(df.duplicated().sum())
    df = df.drop_duplicates()

    print(f"Duplicate rows removed: {duplicate_count}")

    # 3. Check missing values
    missing = df.isnull().sum()
    print("\nMissing values by column:")
    print(missing[missing > 0] if missing.any() else "None")

    # Do not silently fill missing values.
    # Stop if missing data needs an explicit treatment decision.
    if df.isnull().any().any():
        raise ValueError(
            "Missing values found. Review them before continuing."
        )

    # 4. Validate important categorical fields
    expected_categories = {
        "Attrition": {"Yes", "No"},
        "OverTime": {"Yes", "No"},
    }

    for column, expected in expected_categories.items():
        if column not in df.columns:
            raise ValueError(f"Required column missing: {column}")

        actual = set(df[column].unique())
        unexpected = actual - expected

        if unexpected:
            raise ValueError(
                f"Unexpected values in {column}: {unexpected}"
            )

    # 5. Validate numeric business rules
    non_negative_columns = [
        "Age",
        "MonthlyIncome",
        "YearsAtCompany",
        "YearsInCurrentRole",
        "TotalWorkingYears",
    ]

    for column in non_negative_columns:
        if column not in df.columns:
            raise ValueError(f"Required column missing: {column}")

        if not pd.api.types.is_numeric_dtype(df[column]):
            raise TypeError(f"{column} must be numeric")

        if (df[column] < 0).any():
            raise ValueError(
                f"Negative values found in {column}"
            )

    if not df["Age"].between(18, 100).all():
        raise ValueError("Age values outside the expected range.")

    # 6. Confirm Attrition is valid
    if not df["Attrition"].isin(["Yes", "No"]).all():
        raise ValueError("Invalid Attrition category.")

    # 7. Save the prepared dataset
    df.to_csv(OUTPUT_FILE, index=False)

    print("\nData preparation completed.")
    print(f"Final rows: {len(df)}")
    print(f"Final columns: {len(df.columns)}")
    print(f"Output file: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

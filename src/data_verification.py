
from pathlib import Path
import pandas as pd

# Project root directory
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Original CSV file
DATA_FILE = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

def main():
    print("=" * 60)
    print("HR ANALYTICS & EMPLOYEE ATTRITION INTELLIGENCE")
    print("=" * 60)

    # Check dataset path
    if not DATA_FILE.exists():
        print(f"\nERROR: Dataset not found:\n{DATA_FILE}")
        return

    # Load dataset
    df = pd.read_csv(DATA_FILE)

    # 1. Dataset dimensions
    print("\n1. DATASET DIMENSIONS")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    # 2. Preview data
    print("\n2. FIRST FIVE ROWS")
    print(df.head().to_string(index=False))

    # 3. Column names
    print("\n3. COLUMN NAMES")
    for column in df.columns:
        print("-", column)

    # 4. Missing values
    print("\n4. MISSING VALUES")
    missing = df.isnull().sum()
    print(missing[missing > 0] if missing.any()
          else "No missing values found.")

    # 5. Duplicate rows
    print("\n5. DUPLICATE ROWS")
    print(df.duplicated().sum())

    # 6. Attrition distribution
    print("\n6. ATTRITION DISTRIBUTION")
    if "Attrition" in df.columns:
        print(df["Attrition"].value_counts(dropna=False))

        print("\nATTRITION PERCENTAGE")
        print(
            (df["Attrition"].value_counts(normalize=True) * 100)
            .round(2)
        )
    else:
        print("Attrition column not found.")

    # 7. Numerical summary
    print("\n7. NUMERICAL SUMMARY")
    print(df.describe().round(2).to_string())

    print("\nVerification completed.")

if __name__ == "__main__":
    main()

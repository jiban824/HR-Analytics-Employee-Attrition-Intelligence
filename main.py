
from pathlib import Path
import pandas as pd

# 1. Define the project and dataset paths
PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# 2. Check whether the dataset exists
if not DATA_FILE.exists():
    raise FileNotFoundError(
        f"Dataset not found at: {DATA_FILE}\n"
        "Check the filename and ensure the CSV is in data/raw."
    )

# 3. Load the CSV into a Pandas DataFrame
df = pd.read_csv(DATA_FILE)

# 4. Display basic dataset information
print("\n" + "=" * 60)
print("HR ANALYTICS & EMPLOYEE ATTRITION INTELLIGENCE")
print("=" * 60)

print("\n1. DATASET DIMENSIONS")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")

print("\n2. FIRST FIVE EMPLOYEE RECORDS")
print(df.head().to_string(index=False))

print("\n3. COLUMN NAMES")
print(df.columns.tolist())

print("\n4. DATA TYPES AND NON-NULL COUNTS")
df.info()

print("\n5. MISSING VALUES BY COLUMN")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

if missing_values.sum() == 0:
    print("No missing values found.")

print("\n6. DUPLICATE ROWS")
print(f"Duplicate rows: {df.duplicated().sum()}")

print("\n7. NUMERICAL SUMMARY")
print(df.describe().round(2).to_string())

# 8. Verify the attrition distribution
if "Attrition" in df.columns:
    print("\n8. EMPLOYEE ATTRITION DISTRIBUTION")
    print(df["Attrition"].value_counts(dropna=False))

    print("\nATTRITION PERCENTAGES")
    print(
        (df["Attrition"].value_counts(normalize=True) * 100)
        .round(2)
        .astype(str)
        .add("%")
    )

print("\nDataset verification completed.")

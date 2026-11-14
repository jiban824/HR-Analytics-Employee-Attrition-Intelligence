
from pathlib import Path

import pandas as pd
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# 1. PROJECT PATHS
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

OUTPUT_DIR = PROJECT_DIR / "reports" / "eda"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")


# --------------------------------------------------
# 2. LOAD DATA
# --------------------------------------------------

def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}"
        )

    df = pd.read_csv(DATA_FILE)

    required_columns = [
        "Attrition",
        "Department",
        "JobRole",
        "Age",
        "YearsAtCompany",
        "MonthlyIncome",
        "OverTime",
        "JobSatisfaction",
        "WorkLifeBalance",
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    print("=" * 60)
    print("HR ANALYTICS: EXPLORATORY DATA ANALYSIS")
    print("=" * 60)

    print(f"\nTotal employees: {len(df)}")
    print(f"Total columns: {len(df.columns)}")

    # --------------------------------------------------
    # 3. OVERALL ATTRITION KPIs
    # --------------------------------------------------

    total_employees = len(df)
    attrition_count = (df["Attrition"] == "Yes").sum()
    active_count = (df["Attrition"] == "No").sum()

    attrition_rate = (
        attrition_count / total_employees * 100
        if total_employees else 0
    )

    print("\n1. OVERALL ATTRITION")
    print(f"Total employees: {total_employees}")
    print(f"Employees who left: {attrition_count}")
    print(f"Employees who stayed: {active_count}")
    print(f"Overall attrition rate: {attrition_rate:.2f}%")

    # --------------------------------------------------
    # 4. DEPARTMENT ATTRITION
    # --------------------------------------------------

    department_summary = (
        df.groupby("Department")
        .agg(
            TotalEmployees=("Attrition", "size"),
            EmployeesLeft=(
                "Attrition",
                lambda x: (x == "Yes").sum()
            ),
        )
    )

    department_summary["AttritionRate"] = (
        department_summary["EmployeesLeft"]
        / department_summary["TotalEmployees"]
        * 100
    )

    department_summary = department_summary.sort_values(
        "AttritionRate", ascending=False
    )

    print("\n2. ATTRITION BY DEPARTMENT")
    print(department_summary.round(2).to_string())

    department_summary.to_csv(
        OUTPUT_DIR / "department_attrition.csv"
    )

    # --------------------------------------------------
    # 5. ATTRITION BY JOB ROLE
    # --------------------------------------------------

    role_summary = (
        df.groupby("JobRole")
        .agg(
            TotalEmployees=("Attrition", "size"),
            EmployeesLeft=(
                "Attrition",
                lambda x: (x == "Yes").sum()
            ),
        )
    )

    role_summary["AttritionRate"] = (
        role_summary["EmployeesLeft"]
        / role_summary["TotalEmployees"]
        * 100
    )

    role_summary = role_summary.sort_values(
        "AttritionRate", ascending=False
    )

    print("\n3. ATTRITION BY JOB ROLE")
    print(role_summary.round(2).to_string())

    role_summary.to_csv(
        OUTPUT_DIR / "job_role_attrition.csv"
    )

    # --------------------------------------------------
    # 6. COMPARE EMPLOYEES WHO LEFT AND STAYED
    # --------------------------------------------------

    comparison = (
        df.assign(
            AttritionGroup=df["Attrition"].map(
                {"Yes": "Left", "No": "Stayed"}
            )
        )
        .groupby("AttritionGroup")
        .agg(
            EmployeeCount=("Attrition", "size"),
            AverageAge=("Age", "mean"),
            AverageMonthlyIncome=("MonthlyIncome", "mean"),
            AverageYearsAtCompany=("YearsAtCompany", "mean"),
            OvertimePercentage=(
                "OverTime",
                lambda x: (x == "Yes").mean() * 100
            ),
        )
        .round(2)
    )

    print("\n4. LEFT VS STAYED")
    print(comparison.to_string())

    comparison.to_csv(
        OUTPUT_DIR / "left_vs_stayed.csv"
    )

    # --------------------------------------------------
    # 7. CHART 1: OVERALL ATTRITION
    # --------------------------------------------------

    attrition_counts = df["Attrition"].value_counts()

    plt.figure(figsize=(7, 5))
    sns.barplot(
        x=attrition_counts.index,
        y=attrition_counts.values
    )
    plt.title("Employee Attrition: Left vs Stayed")
    plt.xlabel("Attrition")
    plt.ylabel("Number of Employees")
    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "01_overall_attrition.png",
        dpi=150
    )
    plt.close()

    # --------------------------------------------------
    # 8. CHART 2: DEPARTMENT ATTRITION RATE
    # --------------------------------------------------

    plt.figure(figsize=(9, 5))
    sns.barplot(
        data=department_summary.reset_index(),
        x="Department",
        y="AttritionRate"
    )
    plt.title("Attrition Rate by Department")
    plt.xlabel("Department")
    plt.ylabel("Attrition Rate (%)")
    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "02_department_attrition.png",
        dpi=150
    )
    plt.close()

    # --------------------------------------------------
    # 9. CHART 3: JOB ROLE ATTRITION RATE
    # --------------------------------------------------

    plt.figure(figsize=(11, 6))
    role_plot = role_summary.reset_index().sort_values(
        "AttritionRate", ascending=True
    )

    sns.barplot(
        data=role_plot,
        x="AttritionRate",
        y="JobRole"
    )
    plt.title("Attrition Rate by Job Role")
    plt.xlabel("Attrition Rate (%)")
    plt.ylabel("Job Role")
    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "03_job_role_attrition.png",
        dpi=150
    )
    plt.close()

    # --------------------------------------------------
    # 10. CHART 4: AGE DISTRIBUTION
    # --------------------------------------------------

    plt.figure(figsize=(9, 5))
    sns.histplot(
        data=df,
        x="Age",
        hue="Attrition",
        bins=15,
        multiple="layer",
        alpha=0.5
    )
    plt.title("Employee Age Distribution by Attrition")
    plt.xlabel("Age")
    plt.ylabel("Number of Employees")
    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "04_age_distribution.png",
        dpi=150
    )
    plt.close()

    # --------------------------------------------------
    # 11. CHART 5: OVERTIME VS ATTRITION RATE
    # --------------------------------------------------

    overtime_summary = (
        df.groupby("OverTime")
        .agg(
            TotalEmployees=("Attrition", "size"),
            EmployeesLeft=(
                "Attrition",
                lambda x: (x == "Yes").sum()
            ),
        )
    )

    overtime_summary["AttritionRate"] = (
        overtime_summary["EmployeesLeft"]
        / overtime_summary["TotalEmployees"]
        * 100
    )

    print("\n5. ATTRITION BY OVERTIME")
    print(overtime_summary.round(2).to_string())

    overtime_summary.to_csv(
        OUTPUT_DIR / "overtime_attrition.csv"
    )

    plt.figure(figsize=(7, 5))
    sns.barplot(
        data=overtime_summary.reset_index(),
        x="OverTime",
        y="AttritionRate"
    )
    plt.title("Attrition Rate by Overtime Status")
    plt.xlabel("Works Overtime")
    plt.ylabel("Attrition Rate (%)")
    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "05_overtime_attrition.png",
        dpi=150
    )
    plt.close()

    # --------------------------------------------------
    # 12. SAVE ANALYSIS SUMMARY
    # --------------------------------------------------

    summary = pd.DataFrame(
        {
            "Metric": [
                "Total Employees",
                "Employees Who Left",
                "Employees Who Stayed",
                "Attrition Rate (%)",
                "Duplicate Rows",
                "Missing Cells",
            ],
            "Value": [
                total_employees,
                attrition_count,
                active_count,
                round(attrition_rate, 2),
                int(df.duplicated().sum()),
                int(df.isnull().sum().sum()),
            ],
        }
    )

    summary.to_csv(
        OUTPUT_DIR / "eda_summary.csv",
        index=False
    )

    print("\n6. GENERATED FILES")
    print(f"Output folder: {OUTPUT_DIR}")
    print("Created 5 charts and 5 CSV summary files.")
    print("\nEDA completed successfully!")


if __name__ == "__main__":
    main()

# HR-Analytics-Employee-Attrition-Intelligence# 📊 HR Analytics & Employee Attrition Intelligence

An end-to-end Data Analytics project focused on analyzing employee attrition, workforce demographics, work experience, and employee retention using **Python, SQL, SQLite, and Power BI**.

The objective of this project is to transform raw HR data into meaningful business insights that help organizations understand employee turnover patterns and identify areas for improving employee retention.

---

## 📌 Project Overview

Employee attrition is one of the major challenges faced by organizations. High employee turnover can increase recruitment costs, affect productivity, and create difficulties in workforce planning.

This project analyzes the IBM HR Analytics Employee Attrition dataset to identify patterns and trends associated with employee attrition.

The analysis covers employee demographics, department-wise attrition, job roles, overtime, income, career experience, and employee retention.

**Project Type:** End-to-End Data Analytics  
**Domain:** Human Resources Analytics  
**Level:** Beginner / Fresher Portfolio Project

---

## 🎯 Project Objectives

- Analyze overall employee attrition and retention rates.
- Identify departments with higher employee turnover.
- Analyze attrition across different job roles.
- Understand the relationship between overtime and employee attrition.
- Explore employee demographics such as age, gender, and marital status.
- Analyze employee experience and years at the company.
- Compare average monthly income between employees who left and stayed.
- Identify workforce segments that may require further retention investigation.
- Build an interactive Power BI dashboard to communicate business insights.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data verification, cleaning, and exploratory analysis |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| SQL | Data querying and analysis |
| SQLite | Database management |
| Power BI | Interactive dashboards and reporting |
| DAX | Measures and calculated columns |
| VS Code | Development environment |
| Git & GitHub | Version control and project documentation |

---

## 📂 Project Structure

```text
HR-Analytics-Project/
│
├── data/
│   ├── raw/
│   │   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│   │
│   └── processed/
│       ├── hr_employee_attrition_cleaned.csv
│       └── hr_analytics.db
│
├── src/
│   ├── data_verification.py
│   ├── eda_analysis.py
│   ├── clean_data.py
│   ├── sql_analysis.py
│   └── run_sql_file.py
│
├── sql/
│   ├── hr_attrition_analysis.sql
│   └── README.md
│
├── notebooks/
│
├── powerbi/
│   └── HR_Analytics_Dashboard.pbix
│
├── reports/
│   ├── eda/
│   └── initial_findings.md
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📁 Dataset Information

**Dataset:** IBM HR Analytics Employee Attrition & Performance

The dataset contains employee-level information covering demographics, job roles, compensation, work experience, job satisfaction, and attrition status.

**Dataset characteristics:**

- Total employee records: 1,470
- Total columns: 35
- Target variable: `Attrition`
- Attrition categories: Yes and No

### Important Dataset Columns

| Column | Description |
|---|---|
| Age | Employee age |
| Gender | Employee gender |
| Department | Employee department |
| JobRole | Employee job role |
| MonthlyIncome | Monthly employee income |
| OverTime | Whether the employee works overtime |
| YearsAtCompany | Years spent at the company |
| TotalWorkingYears | Total career experience |
| YearsInCurrentRole | Years in the current role |
| YearsWithCurrManager | Years with current manager |
| YearsSinceLastPromotion | Years since last promotion |
| JobSatisfaction | Employee job satisfaction level |
| WorkLifeBalance | Employee work-life balance level |
| Attrition | Whether the employee left the organization |

---

## 🔍 Project Workflow

### 1. Data Verification

- Imported the raw CSV dataset.
- Checked dataset dimensions and column names.
- Inspected missing values.
- Checked duplicate records.
- Examined numerical and categorical variables.
- Reviewed the distribution of the attrition column.

### 2. Data Cleaning

- Removed duplicate records where applicable.
- Checked missing values.
- Validated important categorical values.
- Checked numeric data fields.
- Exported the cleaned dataset.

**Output:** `hr_employee_attrition_cleaned.csv`

### 3. Exploratory Data Analysis (EDA)

Performed exploratory analysis to understand employee attrition patterns.

Analyses included:

- Overall employee attrition.
- Department-wise attrition.
- Job-role-wise attrition.
- Overtime and employee attrition.
- Comparison of employees who left and stayed.
- Average age and monthly income analysis.
- Employee tenure analysis.

### 4. SQL Analysis

Used SQLite to perform structured queries on the cleaned employee dataset.

SQL analysis includes:

1. Overall employee attrition.
2. Department-wise attrition.
3. Job-role-wise attrition.
4. Overtime-based attrition.
5. Tenure-based attrition.
6. Duplicate employee-number validation.
7. Attrition category validation.
8. Invalid age, income, and tenure checks.
9. Additional tenure-based analysis.

**Database:** `hr_analytics.db`  
**Table:** `employees`

### 5. Power BI Dashboard

Developed an interactive HR Analytics dashboard using Power BI.

The dashboard is organized into four analytical pages.

#### Page 1 — Executive Overview

Focus: Overall workforce and attrition performance.

KPIs:
- Total Employees
- Employees Left
- Employees Stayed
- Attrition Rate

Analysis:
- Employee attrition distribution.
- Department-wise workforce analysis.
- Overtime and attrition comparison.
- Employee retention overview.

#### Page 2 — Department & Job Role Analysis

Focus: Understanding attrition across organizational structures.

KPIs:
- Highest Department Attrition Rate
- Highest Job Role Attrition Rate
- Employees Left in Sales
- Sales Representative Attrition Count

Analysis:
- Attrition by job role.
- Department-wise employee departures.
- Gender-based department analysis.
- Business travel and attrition.

#### Page 3 — Employee Demographics

Focus: Understanding employee attrition across demographic groups.

KPIs:
- Average Age of Employees Who Left
- Average Age of Employees Who Stayed
- Female Employees
- Male Employees

Analysis:
- Age-group-wise attrition.
- Gender-based attrition.
- Marital-status analysis.
- Education-field analysis.

#### Page 4 — Work Experience & Retention

Focus: Understanding the relationship between employee experience, tenure, and retention.

KPIs:
- Average Years at Company — Left
- Average Years at Company — Stayed
- Average Total Working Years — Left
- Average Total Working Years — Stayed

Analysis:
- Attrition by company tenure.
- Attrition by total working experience.
- Attrition by years in current role.
- Attrition by years with current manager.

---

## 📈 Key Performance Indicators (KPIs)

The project includes the following important HR metrics:

| KPI | Description |
|---|---|
| Total Employees | Total employee records |
| Employees Left | Number of employees who left |
| Employees Stayed | Number of employees who remained |
| Attrition Rate | Percentage of employees who left |
| Average Monthly Income | Average employee monthly income |
| Average Age | Average age of employees |
| Average Years at Company | Average employee tenure |
| Average Total Working Years | Average career experience |

### Important DAX Measures

**Total Employees**

```dax
Total Employees =
COUNTROWS(Employees)
```

**Employees Left**

```dax
Employees Left =
CALCULATE(
    COUNTROWS(Employees),
    Employees[Attrition] = "Yes"
)
```

**Attrition Rate**

```dax
Attrition Rate =
DIVIDE(
    [Employees Left],
    [Total Employees],
    0
)
```

**Average Years at Company**

```dax
Average Years at Company =
AVERAGE(Employees[YearsAtCompany])
```

**Average Total Working Years**

```dax
Average Total Working Years =
AVERAGE(Employees[TotalWorkingYears])
```

---

## 📊 Key Business Findings

Based on the exploratory analysis of the dataset:

| Metric | Result |
|---|---:|
| Total Employees | 1,470 |
| Employees Who Left | 237 |
| Employees Who Stayed | 1,233 |
| Overall Attrition Rate | 16.12% |
| Sales Department Attrition | 20.63% |
| Human Resources Attrition | 19.05% |
| Research & Development Attrition | 13.84% |
| Sales Representative Attrition | 39.76% |
| Laboratory Technician Attrition | 23.94% |
| Attrition with Overtime | 30.53% |
| Attrition without Overtime | 10.44% |

### Work Experience & Retention Findings

| Experience Metric | Left | Stayed |
|---|---:|---:|
| Average Years at Company | 5.13 | 7.37 |
| Average Total Working Years | 8.24 | 11.86 |
| Average Years in Current Role | 2.90 | 4.48 |
| Average Years with Current Manager | 2.85 | 4.37 |

### Major Observations

1. The overall employee attrition rate is 16.12%.
2. The Sales department has the highest department-level attrition rate.
3. Sales Representatives have the highest job-role attrition rate.
4. Employees working overtime have a higher attrition rate than employees not working overtime.
5. Employees who left have lower average company tenure than employees who stayed.
6. Employees with shorter career experience show higher attrition rates in the analyzed experience groups.

These observations represent associations in the dataset and do not establish causation.

---

## 💡 Business Recommendations

Based on the analysis, organizations could investigate the following areas:

- Review employee retention strategies in departments with higher attrition.
- Investigate workload and overtime patterns.
- Improve onboarding and support for employees in their early tenure.
- Review career growth and internal promotion opportunities.
- Evaluate employee satisfaction and work-life balance.
- Strengthen manager-employee engagement.
- Monitor compensation and employee development opportunities.
- Regularly track attrition KPIs to identify emerging workforce trends.

---

## 🚀 How to Run This Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd HR-Analytics-Project
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 5: Install Required Packages

```bash
pip install -r requirements.txt
```

### Step 6: Run Data Verification

```bash
python src/data_verification.py
```

### Step 7: Run Exploratory Data Analysis

```bash
python src/eda_analysis.py
```

### Step 8: Clean the Dataset

```bash
python src/clean_data.py
```

### Step 9: Run SQL Analysis

```bash
python src/sql_analysis.py
```

### Step 10: Execute SQL Queries

```bash
python src/run_sql_file.py
```

### Step 11: Open the Power BI Dashboard

Open the `.pbix` file from the `powerbi` folder using Power BI Desktop.

---

## 📚 Skills Demonstrated

Through this project, I worked on:

- Data Cleaning and Preprocessing
- Exploratory Data Analysis
- Data Validation
- SQL Query Writing
- SQLite Database Management
- Data Visualization
- DAX Measures and Calculated Columns
- Power BI Dashboard Development
- KPI Development
- Business Insights and Recommendations
- Data Storytelling

---

## ⚠️ Limitations

- The analysis is based on the provided IBM HR Analytics dataset.
- The findings are descriptive and do not establish causal relationships.
- The dataset may not represent every organization's workforce.
- Some employee groups have relatively small sample sizes, so their attrition rates should be interpreted carefully.
- The dataset does not establish a currency for monthly income.

---

## 👨‍💻 Author

**HR Analytics & Employee Attrition Intelligence**

Developed as an end-to-end Data Analytics portfolio project to demonstrate practical skills in Python, SQL, SQLite, Power BI, and business intelligence.

---

⭐ If you find this project useful, feel free to star the repository!

**Technologies:** Python | Pandas | NumPy | Matplotlib | Seaborn | SQL | SQLite | Power BI | DAX

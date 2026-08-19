🔥 Day 46 — Pandas Data Transformation
🎯 Objective

Learn how to transform Pandas DataFrames by creating new columns, performing calculations, applying conditions, using custom functions, mapping categorical values, and building a basic ETL-style transformation pipeline.

📚 Topics Covered
1. Creating New Columns

New columns can be created using:

df["new_column"] = ...

Example:

df["annual_bonus"] = df["salary"] * 0.10

This creates a new column containing 10% of the salary.

2. Vectorized Operations

Pandas allows operations to be performed directly on entire columns without manually using a for loop.

Example:

df["bonus"] = df["salary"] * 0.10

For:

salary
50000
60000
70000

The result is:

bonus
5000
6000
7000
Common vectorized operations
df["salary"] + 5000
df["salary"] * 1.10
df["salary"] / 12
df["salary"] - df["tax"]

Vectorized operations are important because they allow Pandas to process entire columns efficiently.

3. Creating Columns from Multiple Columns

A new column can be created using multiple existing columns.

Example:

df["total_compensation"] = df["salary"] + df["bonus"]

Another example:

df["net_salary"] = (
    df["salary"] +
    df["bonus"] -
    df["tax"]
)

Pandas performs these calculations row by row using the DataFrame index.

Example:

salary | bonus | total
50000  | 5000  | 55000
60000  | 6000  | 66000
70000  | 7000  | 77000
4. Boolean Conditions

We can check conditions directly on a Pandas column.

Example:

df["salary"] >= 70000

This produces Boolean values:

False
False
True
True

Boolean conditions are useful for filtering and conditional transformations.

5. np.where()

np.where() is useful for simple conditional transformations.

First import NumPy:

import numpy as np

Syntax:

np.where(
    condition,
    value_if_true,
    value_if_false
)

Example:

df["salary_category"] = np.where(
    df["salary"] >= 70000,
    "High",
    "Normal"
)

Result:

salary | salary_category
45000  | Normal
55000  | Normal
70000  | High
85000  | High
Important

np.where() is especially useful when there are two possible outcomes:

condition → True value
otherwise → False value
6. apply()

apply() is used to apply a function to values in a Pandas Series.

Example:

def classify_salary(salary):
    if salary < 50000:
        return "Low"
    elif salary < 70000:
        return "Medium"
    elif salary < 90000:
        return "High"
    else:
        return "Very High"

Then:

df["salary_category"] = df["salary"].apply(
    classify_salary
)

The function is applied to each salary value.

Example:

45000 → Low
55000 → Medium
70000 → High
85000 → High
95000 → Very High
7. apply() with Multiple Conditions

apply() becomes useful when the transformation contains multiple rules.

Example:

def classify_salary(salary):
    if salary < 50000:
        return "Low"
    elif salary < 70000:
        return "Medium"
    elif salary < 90000:
        return "High"
    else:
        return "Very High"

This is more flexible than a simple np.where() condition.

8. lambda

A lambda function is a small anonymous function.

Example:

lambda salary: salary * 0.10

This means:

Take salary and return salary * 0.10.

It can be used with apply():

df["bonus"] = df["salary"].apply(
    lambda salary: salary * 0.10
)
9. Salary Raise Using lambda

To calculate salary after a 15% raise:

df["salary_after_raise"] = df["salary"].apply(
    lambda salary: salary * 1.15
)
Important distinction
salary * 0.15

means:

15% of the salary

while:

salary * 1.15

means:

salary after a 15% raise

Example:

50000 × 1.15 = 57500
10. map()

map() is useful for value-to-value mapping.

It is especially useful for categorical transformations.

Example:

department_map = {
    "IT": "Technology",
    "HR": "Human Resources",
    "Finance": "Financial Services"
}

Then:

df["department_full"] = df["department"].map(
    department_map
)

Result:

IT       → Technology
HR       → Human Resources
Finance  → Financial Services
11. map() with Dictionary

A common Data Engineering pattern is:

mapping = {
    "short_value": "long_value"
}


df["new_column"] = df["column"].map(mapping)

For example:

department_map = {
    "IT": "Technology",
    "HR": "Human Resources"
}


df["department_full"] = df["department"].map(
    department_map
)
12. What Happens When a Mapping Doesn't Exist?

If a value is not present in the dictionary, map() returns NaN.

Example:

department_map = {
    "IT": "Technology",
    "HR": "Human Resources"
}

If the DataFrame contains:

IT
HR
Finance

Then:

df["department"].map(department_map)

returns:

Technology
Human Resources
NaN

This is important when working with real-world datasets containing unexpected categories.

🔑 map() vs apply()
map()

Best suited for:

Value → Mapped Value

Example:

department_map = {
    "IT": "Technology",
    "HR": "Human Resources"
}
df["department"].map(department_map)
apply()

Best suited for:

Value → Custom Function → Result

Example:

df["salary"].apply(classify_salary)
Simple rule
map()
→ Dictionary/value mapping


apply()
→ Custom logic/function
🧹 Day 44 + Day 45 + Day 46 Data Workflow

We can now build a basic data-cleaning and transformation pipeline.

Raw Dataset
     ↓
Inspect Dataset
     ↓
head()
info()
describe()
     ↓
Check Missing Values
     ↓
isnull().sum()
     ↓
Handle Missing Values
     ↓
fillna() / dropna()
     ↓
Find Duplicates
     ↓
duplicated()
     ↓
Remove Duplicates
     ↓
drop_duplicates()
     ↓
Transform Data
     ↓
Vectorized Operations
np.where()
apply()
lambda
map()
     ↓
Validate
     ↓
isnull().sum()
duplicated().sum()
     ↓
Final Dataset
💻 Final Day 46 Mini ETL Example
import pandas as pd
import numpy as np


df = pd.DataFrame({
    "employee_id": [101, 102, 103, 104, 105],
    "name": ["Rahul", "Priya", "Amit", "Sneha", "Raj"],
    "salary": [45000, 55000, 70000, 85000, 95000],
    "department": ["IT", "HR", "Finance", "IT", "HR"]
})


# Create bonus
df["bonus"] = df["salary"] * 0.10


# Create total compensation
df["total_compensation"] = (
    df["salary"] + df["bonus"]
)


# Create salary category
df["salary_category"] = np.where(
    df["salary"] >= 70000,
    "High",
    "Normal"
)


# Calculate salary after 15% raise
df["salary_after_raise"] = df["salary"].apply(
    lambda salary: salary * 1.15
)


# Department mapping
department_map = {
    "IT": "Technology",
    "HR": "Human Resources",
    "Finance": "Financial Services"
}


df["department_full"] = df["department"].map(
    department_map
)


print(df)
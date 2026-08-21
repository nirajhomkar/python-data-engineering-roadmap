🔥 Day 47 — Pandas String Operations & Text Cleaning
🎯 Objective

Learn how to clean, standardize, transform, and filter string/text columns in Pandas using the .str accessor.

📚 Topics Covered
1. .str.lower()

Converts strings to lowercase.

df["name"] = df["name"].str.lower()

Example:

RAHUL → rahul
Priya → priya
AMIT  → amit
2. .str.upper()

Converts strings to uppercase.

df["department"] = df["department"].str.upper()

Example:

it → IT
Hr → HR
finance → FINANCE
3. .str.title()

Converts text to Title Case.

df["name"] = df["name"].str.title()

Example:

rahul homkar → Rahul Homkar
PRIYA → Priya
amit kumar → Amit Kumar
4. .str.strip()

Removes leading and trailing whitespace.

df["name"] = df["name"].str.strip()

Example:

" Rahul " → "Rahul"
" Priya"  → "Priya"
"Amit "   → "Amit"

It does not remove spaces between words.

"Rahul Homkar" → "Rahul Homkar"
5. .str.len()

Returns the number of characters in each string.

df["name"].str.len()

Example:

Rahul → 5
Priya → 5
Amit  → 4

Useful for data validation.

6. .str.contains()

Checks whether a string contains a particular value.

df["name"].str.contains("Rahul")

Example:

Rahul        → True
Priya        → False
Rahul Kumar  → True
Amit         → False

Can also be used for filtering:

df[df["name"].str.contains("Rahul")]
7. .str.replace()

Replaces or removes text.

Syntax:

df["column"].str.replace("old", "new")

Example:

df["phone"].str.replace("-", "")
987-654-3210 → 9876543210
8. .str.split()

Splits a string into multiple parts.

df["full_name"].str.split(" ")

Example:

Rahul Homkar → ["Rahul", "Homkar"]

We can extract individual parts:

df["full_name"].str.split(" ").str[0]

➡️ First name

df["full_name"].str.split(" ").str[1]

➡️ Last name

9. .str.startswith()

Checks whether a string starts with a particular value.

df["email"].str.startswith("rahul")
10. .str.endswith()

Checks whether a string ends with a particular value.

df["email"].str.endswith("@gmail.com")

Example:

rahul@gmail.com    → True
priya@yahoo.com    → False
amit@gmail.com     → True
🔑 Important .str Pattern

For Pandas string columns:

.str.lower()
.str.upper()
.str.title()
.str.strip()
.str.len()
.str.contains()
.str.replace()
.str.split()
.str.startswith()
.str.endswith()

The .str accessor allows us to apply string operations to an entire Pandas Series.

🔗 Chaining String Operations

Multiple operations can be chained together.

Example:

df["name"] = df["name"].str.strip().str.title()

This:

1. Removes spaces
2. Converts to Title Case

Another example:

df["department"] = df["department"].str.strip().str.upper()

This:

1. Removes spaces
2. Converts to uppercase
🧹 Day 47 ETL Pattern
Raw Text
   ↓
strip()
   ↓
lower()/upper()/title()
   ↓
replace()
   ↓
split()
   ↓
contains()/startswith()/endswith()
   ↓
Filter / Transform
   ↓
Clean Data
💻 Day 47 Mini ETL Pipeline
import pandas as pd
import numpy as np


df = pd.DataFrame({
    "employee_id": [101, 102, 103, 101, 104, 105],
    "name": [" Rahul ", "PRIYA", " Amit ", "Rahul", "Sneha", "RAJ"],
    "email": [
        "rahul@gmail.com",
        "priya@yahoo.com",
        "amit@gmail.com",
        "rahul@gmail.com",
        "sneha@outlook.com",
        "raj@gmail.com"
    ],
    "department": [" IT ", "hr", "FINANCE", " IT", "HR ", "it"],
    "salary": [50000, 60000, None, 55000, 65000, None]
})


# Clean name
df["name"] = df["name"].str.strip().str.title()


# Clean department
df["department"] = df["department"].str.strip().str.upper()


# Check Gmail
df["is_gmail"] = df["email"].str.endswith("@gmail.com")


# Handle missing salary
df["salary"] = df["salary"].fillna(df["salary"].median())


# Remove duplicate employees
df = df.drop_duplicates(
    subset=["employee_id"],
    keep="last"
)


# Calculate bonus
df["annual_bonus"] = df["salary"] * 0.10


# Salary category
df["salary_category"] = np.where(
    df["salary"] >= 60000,
    "High",
    "Normal"
)


# Filter Gmail employees
gmail_employees = df[df["is_gmail"]]


# Validate
print(gmail_employees.isnull().sum())
print(
    gmail_employees.duplicated(
        subset=["employee_id"]
    ).sum()
)
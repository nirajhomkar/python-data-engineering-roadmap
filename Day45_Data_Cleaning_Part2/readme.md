# 🔥 Day 45 — Pandas Duplicate Data & Data Quality

## 🎯 Objective

Learn how to detect duplicate records, remove duplicates safely, control which duplicate record is retained, and combine duplicate handling with missing-value cleaning.

---

## 📚 Topics Covered

### 1. `duplicated()`

Used to identify duplicate rows.

```python
df.duplicated()
```

By default, Pandas checks the **entire row**.

Example:

```text
False
False
False
True
```

* `False` → not a duplicate occurrence
* `True` → duplicate occurrence

---

### 2. `duplicated(subset=...)`

Duplicates can be checked using specific columns.

```python
df.duplicated(subset=["employee_id"])
```

This checks duplication based only on `employee_id`.

This is useful when `employee_id` should uniquely identify an employee.

---

### 3. `duplicated(keep=False)`

By default, only later occurrences are marked as duplicates.

```python
df.duplicated(subset=["employee_id"])
```

Example:

```text
employee_id
101
102
101
```

Output:

```text
False
False
True
```

Using:

```python
df.duplicated(
    subset=["employee_id"],
    keep=False
)
```

Output:

```text
True
False
True
```

`keep=False` marks **every row involved in a duplicate group** as `True`.

---

## 4. Counting Duplicate Rows

Boolean values can be counted using `sum()`.

```python
df.duplicated().sum()
```

For a specific column:

```python
df.duplicated(
    subset=["employee_id"]
).sum()
```

Example:

```text
2
```

means there are two duplicate occurrences.

---

## 5. `drop_duplicates()`

Used to remove duplicate rows.

```python
clean_df = df.drop_duplicates()
```

By default, the first occurrence is kept.

---

## 6. `subset` with `drop_duplicates()`

To remove duplicates based on a specific column:

```python
clean_df = df.drop_duplicates(
    subset=["employee_id"]
)
```

This checks duplicates based only on `employee_id`.

---

## 7. `keep="first"`

This is the default behavior.

```python
df.drop_duplicates(
    subset=["employee_id"],
    keep="first"
)
```

Keeps the first occurrence and removes later duplicates.

Example:

```text
101 | Rahul | 50000
101 | Rahul | 55000
```

Result:

```text
101 | Rahul | 50000
```

---

## 8. `keep="last"`

Keeps the last occurrence.

```python
df.drop_duplicates(
    subset=["employee_id"],
    keep="last"
)
```

Example:

```text
101 | Rahul | 50000
101 | Rahul | 55000
```

Result:

```text
101 | Rahul | 55000
```

This is useful when the latest record contains updated information.

---

## 9. `keep=False`

Using:

```python
df.drop_duplicates(
    subset=["employee_id"],
    keep=False
)
```

removes **all occurrences** of duplicated values.

For example:

```text
101
102
101
103
```

After `keep=False`:

```text
102
103
```

Both `101` records are removed.

---

# 🔹 `duplicated()` vs `drop_duplicates()`

```text
duplicated()
        ↓
Find duplicate records

drop_duplicates()
        ↓
Remove duplicate records
```

Remember:

```python
df.duplicated()
```

does not remove anything.

It only identifies duplicates.

---

# 🔹 `keep` Options

| Option         | Behavior                          |
| -------------- | --------------------------------- |
| `keep="first"` | Keep first occurrence             |
| `keep="last"`  | Keep last occurrence              |
| `keep=False`   | Remove all duplicated occurrences |

---

# 🧹 Combining Day 44 + Day 45

We can now perform a basic real-world data-cleaning workflow.

```text
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
Validate
     ↓
isnull().sum()
duplicated().sum()
```

---

# 💡 Important Data Engineering Pattern

Suppose an employee can have multiple records:

```text
employee_id | salary
101         | 50000
101         | 55000
```

If the latest record should be retained:

```python
clean_df = df.drop_duplicates(
    subset=["employee_id"],
    keep="last"
).copy()
```

The `.copy()` creates an independent DataFrame that can safely be modified.

---

# ⚠️ `SettingWithCopyWarning`

When working with DataFrame slices or results of filtering operations, Pandas may produce:

```text
SettingWithCopyWarning
```

A useful practice is:

```python
clean_df = df[condition].copy()
```

or:

```python
clean_df = df.drop_duplicates(
    subset=["employee_id"],
    keep="last"
).copy()
```

This explicitly creates an independent DataFrame.

---

# 🧮 Combining Duplicates with Missing Values

After removing duplicates, we can handle missing values.

For example:

```python
clean_df["salary"] = clean_df["salary"].fillna(
    clean_df["salary"].median()
)
```

For categorical data:

```python
clean_df["department"] = clean_df["department"].fillna(
    "Unknown"
)
```

---

# 💻 Final Day 45 Example

```python
import pandas as pd

df = pd.DataFrame({
    "employee_id": [101, 102, 103, 101, 104, 103, 105],
    "name": ["Rahul", "Priya", "Amit", "Rahul", "Sneha", "Amit", "Raj"],
    "salary": [50000, 60000, None, 55000, 65000, 72000, None],
    "department": ["IT", "HR", "IT", "IT", "Finance", "IT", None]
})

# Check missing values
print(df.isnull().sum())

# Find all records involved in duplicate employee IDs
duplicate = df.duplicated(
    subset=["employee_id"],
    keep=False
)

print(duplicate.sum())

# Remove duplicates and keep the latest record
clean_df = df.drop_duplicates(
    subset=["employee_id"],
    keep="last"
).copy()

# Fill missing salary with median
clean_df["salary"] = clean_df["salary"].fillna(
    clean_df["salary"].median()
)

# Fill missing department
clean_df["department"] = clean_df["department"].fillna(
    "Unknown"
)

# Display cleaned data
print(clean_df)

# Validate missing values
print(clean_df.isnull().sum())

# Validate duplicate employee IDs
print(
    clean_df.duplicated(
        subset=["employee_id"]
    ).sum()
)
```

---

# 🧠 Key Takeaways

```text
duplicated()
→ Detect duplicate rows

duplicated(subset=...)
→ Detect duplicates based on selected columns

duplicated(keep=False)
→ Mark every row involved in a duplicate group

drop_duplicates()
→ Remove duplicate rows

drop_duplicates(subset=...)
→ Remove duplicates based on selected columns

keep="first"
→ Keep first occurrence

keep="last"
→ Keep last occurrence

keep=False
→ Remove all duplicate occurrences

.copy()
→ Create an independent DataFrame
```

---

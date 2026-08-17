# 🔥 Day 44 — Pandas Data Cleaning & Missing Values

## 🎯 Objective

Learn how to identify, remove, and replace missing values in Pandas DataFrames and apply these techniques to a realistic employee dataset.

---

## 📚 Topics Covered

### 1. Missing Values

Missing values are common in real-world datasets.

Pandas commonly represents missing numerical values as `NaN`.

Example:

```python
salary
50000
NaN
60000
```

Missing data must be investigated and handled before reliable analysis.

---

### 2. `isnull()`

Used to identify missing values.

```python
df.isnull()
```

Returns:

```text
True  → missing
False → not missing
```

To count missing values in each column:

```python
df.isnull().sum()
```

---

### 3. `isna()`

`isna()` performs the same missing-value detection as `isnull()`.

```python
df.isna()
```

Counting missing values:

```python
df.isna().sum()
```

---

### 4. `notnull()`

Checks whether values are present.

```python
df["salary"].notnull()
```

Returns:

```text
True  → value exists
False → value is missing
```

It can also be used for Boolean filtering:

```python
df[df["salary"].notnull()]
```

---

### 5. `dropna()`

Removes rows containing missing values.

```python
df.dropna()
```

By default, rows containing at least one missing value are removed.

---

### 6. `dropna(subset=...)`

Allows us to check only selected columns.

```python
df.dropna(subset=["salary"])
```

This removes rows where `salary` is missing while allowing missing values in other columns.

---

### 7. `fillna()`

Used to replace missing values.

Example:

```python
df["salary"].fillna(0)
```

Replace missing salaries with zero.

For categorical values:

```python
df["department"].fillna("Unknown")
```

---

### 8. Assigning `fillna()` Back

`fillna()` does not modify the original object by default.

Therefore:

```python
df["salary"].fillna(0)
```

does not permanently change `df`.

To update the DataFrame:

```python
df["salary"] = df["salary"].fillna(0)
```

---

## 📊 Mean vs Median

### Mean

Mean calculates the average.

```python
df["salary"].mean()
```

It can be strongly affected by extreme values.

### Median

Median gives the middle value after sorting.

```python
df["salary"].median()
```

It is less affected by extreme outliers.

Example:

```text
30000
40000
50000
60000
500000
```

Mean = 136000

Median = 50000

Therefore, median can be a better choice when numerical data contains significant outliers.

---

## 🧹 Real Data Cleaning Workflow

A practical workflow learned today:

```text
Inspect dataset
      ↓
head()
tail()
info()
describe()
      ↓
Check missing values
      ↓
isnull().sum()
      ↓
Understand why data is missing
      ↓
Choose cleaning strategy
      ↓
dropna() / fillna()
      ↓
Validate cleaned data
      ↓
isnull().sum()
```

---

## 💻 Final Coding Example

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Rahul", "Priya", "Amit", "Sneha", "Raj"],
    "salary": [50000, None, 60000, None, 70000],
    "department": ["IT", "HR", None, "IT", None],
    "age": [25, None, 28, 30, None]
})

print(df.isnull().sum())

df["salary"] = df["salary"].fillna(df["salary"].median())
df["department"] = df["department"].fillna("Unknown")
df["age"] = df["age"].fillna(df["age"].median())

print(df)

print(df.isnull().sum())
```

Final validation should show:

```text
name          0
salary        0
department    0
age           0
```

---

## 🧠 Key Takeaways

```text
isnull()       → detect missing values
isna()         → detect missing values
notnull()      → detect existing values
dropna()       → remove missing-data rows/columns
fillna()       → replace missing values
mean()         → average
median()       → middle value
```

Important distinction:

```text
dropna() → remove data
fillna() → replace data
```

For numerical columns, choose a replacement strategy based on the nature of the data.

For categorical columns, values such as `"Unknown"` can be appropriate when the missing category has no reliable replacement.

---

## 🏆 Day 44 Result

* Missing values: ✅
* `isnull()`: ✅
* `isna()`: ✅
* `notnull()`: ✅
* `dropna()`: ✅
* `dropna(subset=...)`: ✅
* `fillna()`: ✅
* Mean vs median: 🟡 Continue practicing
* Real dataset cleaning: ✅
* Final coding challenge: ✅
* Final quiz: 5/6
* Reflection: ✅

### Overall Score: 9/10

**Day 44 — COMPLETE ✅🔥**

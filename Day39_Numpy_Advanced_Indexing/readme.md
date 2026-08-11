# Day 39 - NumPy Advanced Indexing

## 📖 Overview

Today I learned advanced indexing techniques in NumPy for selecting specific elements, rows, columns, and coordinates, as well as using `np.where()` for filtering and data transformation.

---

## 📚 Topics Covered

- Integer/Fancy Indexing
- Multiple index selection
- 2D row selection
- Row and column coordinate selection
- Boolean indexing
- `np.where()`
- Conditional transformation using `np.where()`
- 2D column selection

---

## 1. Integer/Fancy Indexing

Multiple elements can be selected using an array or list of indexes.

```python
import numpy as np

arr = np.array([10,20,30,40,50])

print(arr[[0,2,4]])
```

Output:

```text
[10 30 50]
```

---

## 2. Selecting Multiple Rows

For a 2D array:

```python
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(arr[[0,2]])
```

Output:

```text
[[10 20 30]
 [70 80 90]]
```

This selects rows 0 and 2.

---

## 3. Selecting Specific Coordinates

Rows and columns can be provided together.

```python
rows = [0,1,2]
cols = [2,1,0]

print(arr[rows, cols])
```

The coordinate pairs are:

```text
(0,2)
(1,1)
(2,0)
```

Output:

```text
[30 50 70]
```

---

## 4. Boolean Indexing

Boolean indexing returns the values that satisfy a condition.

```python
arr = np.array([10,20,30,40,50])

print(arr[arr > 30])
```

Output:

```text
[40 50]
```

---

## 5. np.where()

`np.where(condition)` returns the indexes where the condition is true.

```python
arr = np.array([10,20,30,40,50,60])

indexes = np.where(arr > 30)

print(indexes)
```

Output:

```text
(array([3, 4, 5]),)
```

The actual values can then be obtained using:

```python
print(arr[indexes])
```

Output:

```text
[40 50 60]
```

---

## 6. np.where() for Transformation

`np.where()` can also transform/classify data.

Syntax:

```python
np.where(condition, value_if_true, value_if_false)
```

Example:

```python
salaries = np.array([30000,45000,60000,75000,90000])

result = np.where(
    salaries >= 60000,
    "High",
    "Low"
)

print(result)
```

Output:

```text
['Low' 'Low' 'High' 'High' 'High']
```

---

## 7. Selecting Columns from 2D Arrays

For a 2D array:

```python
arr[rows, columns]
```

The `:` means all rows.

Example:

```python
arr[:, 1]
```

means:

```text
All rows
+
Second column
```

Column indexing starts from 0:

```text
0 → first column
1 → second column
2 → third column
```

---

## 🌍 Data Engineering Example

Advanced indexing can be useful when selecting specific records or filtering employees based on conditions such as salary.

Example:

```python
employees = np.array([
    [101,50000,2],
    [102,75000,4],
    [103,60000,3],
    [104,90000,5]
])

salaries = employees[:,1]

high_salary = employees[salaries >= 60000]

print(high_salary)
```

This demonstrates selecting data based on a salary condition.

---

## 💡 Key Learnings

- Integer indexing allows multiple indexes to be selected at once.
- `arr[[0,2,4]]` selects specific elements.
- `arr[[0,2]]` can select specific rows from a 2D array.
- `arr[rows, cols]` selects specific coordinate pairs.
- Boolean indexing returns matching values.
- `np.where(condition)` returns matching indexes.
- `np.where(condition, true, false)` transforms data based on a condition.
- `arr[:,1]` selects the second column from all rows.
- NumPy indexing starts from 0.

---

## 🎯 Interview Questions

### What is fancy indexing?

Fancy indexing allows multiple elements to be selected using an array or list of indexes.

### What is the difference between Boolean indexing and np.where()?

Boolean indexing returns matching values, while `np.where(condition)` returns the indexes where the condition is true.

### What does np.where(condition, true, false) do?

It creates a new array by selecting one value when the condition is true and another value when it is false.

### What does `arr[:,1]` mean?

It selects the second column from all rows.

---

## 📈 NumPy Progress

- ✅ Day 31 - NumPy Fundamentals
- ✅ Day 32 - Array Creation
- ✅ Day 33 - Mathematical Operations
- ✅ Day 34 - Boolean Indexing & Filtering
- ✅ Day 35 - Random Module
- ✅ Day 36 - Broadcasting
- ✅ Day 37 - Array Manipulation
- ✅ Day 38 - Stacking & Splitting
- ✅ Day 39 - Advanced Indexing
- ⏳ Day 40 - NumPy Mini Project

---

## 💻 Technologies Used

- Python
- NumPy
- Jupyter Notebook
- Git & GitHub
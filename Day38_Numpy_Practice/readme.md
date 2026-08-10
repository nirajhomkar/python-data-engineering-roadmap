# Day 38 - NumPy Stacking & Splitting

## 📖 Overview

Today I learned how to combine and split NumPy arrays using concatenation, stacking, and splitting operations.

---

## 📚 Topics Covered

- `np.concatenate()`
- `axis=0`
- `axis=1`
- `np.vstack()`
- `np.hstack()`
- `np.split()`
- `np.array_split()`
- Batch processing concept
- Combining datasets

---

## 1. np.concatenate()

`np.concatenate()` combines arrays together.

```python
import numpy as np

arr1 = np.array([10,20,30])
arr2 = np.array([40,50,60])

result = np.concatenate((arr1, arr2))

print(result)
```

Output:

```text
[10 20 30 40 50 60]
```

---

## 2. Concatenation with axis

For 2D arrays:

### axis=0

`axis=0` adds rows.

```python
result = np.concatenate((arr1, arr2), axis=0)
```

Conceptually:

```text
axis=0 → rows
```

### axis=1

`axis=1` adds columns.

```python
result = np.concatenate((arr1, arr2), axis=1)
```

Conceptually:

```text
axis=1 → columns
```

---

## 3. np.vstack()

`vstack()` means vertical stacking.

```python
a = np.array([10,20,30])
b = np.array([40,50,60])

result = np.vstack((a,b))

print(result)
```

Output:

```text
[[10 20 30]
 [40 50 60]]
```

Shape:

```text
(2,3)
```

For compatible 2D arrays, `vstack()` adds rows.

---

## 4. np.hstack()

`hstack()` means horizontal stacking.

```python
a = np.array([10,20,30])
b = np.array([40,50,60])

result = np.hstack((a,b))

print(result)
```

Output:

```text
[10 20 30 40 50 60]
```

For compatible 2D arrays, `hstack()` adds columns.

---

## 5. np.split()

`np.split()` divides an array into equal-sized sections.

```python
arr = np.array([10,20,30,40,50,60])

parts = np.split(arr, 3)

print(parts)
```

Output:

```text
[array([10,20]), array([30,40]), array([50,60])]
```

The array must be divisible into equal sections.

---

## 6. np.array_split()

`array_split()` allows sections of unequal size.

```python
arr = np.array([1,2,3,4,5])

parts = np.array_split(arr, 2)

print(parts)
```

Possible output:

```text
[array([1,2,3]), array([4,5])]
```

### Difference

```text
np.split()
→ Equal-sized sections required

np.array_split()
→ Unequal-sized sections allowed
```

---

## 🌍 Data Engineering Example

Datasets can be combined and divided into batches for processing.

```python
sales_jan = np.array([
    [101,500],
    [102,700],
    [103,300]
])

sales_feb = np.array([
    [104,800],
    [105,600]
])

all_sales = np.vstack((sales_jan, sales_feb))

batches = np.array_split(all_sales, 2)
```

This demonstrates a simple batch-processing workflow:

```text
Multiple datasets
       ↓
Combine
       ↓
Split into batches
       ↓
Process batches
       ↓
Combine processed data
```

---

## 💡 Key Learnings

- `concatenate()` combines arrays.
- `axis=0` works along rows for 2D concatenation.
- `axis=1` works along columns for 2D concatenation.
- `vstack()` performs vertical stacking.
- `hstack()` performs horizontal stacking.
- `split()` requires equal-sized sections.
- `array_split()` allows unequal-sized sections.
- Stacking and splitting are useful concepts for data processing and batch processing.

---

## 🎯 Interview Questions

### What is `np.concatenate()`?

It combines multiple arrays along a specified axis.

### What is the difference between `vstack()` and `hstack()`?

`vstack()` adds rows, while `hstack()` adds columns for compatible 2D arrays.

### What is the difference between `split()` and `array_split()`?

`split()` requires equal-sized sections, while `array_split()` can create unequal-sized sections.

### What does axis=0 mean?

For 2D concatenation, `axis=0` adds rows.

### What does axis=1 mean?

For 2D concatenation, `axis=1` adds columns.

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
- ⏳ Day 39 - Advanced Indexing
- ⏳ Day 40 - NumPy Mini Project

---

## 💻 Technologies Used

- Python
- NumPy
- Jupyter Notebook
- Git & GitHub
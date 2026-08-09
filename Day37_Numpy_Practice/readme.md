# Day 37 - NumPy Array Manipulation

## 📖 Overview

Today I learned how to manipulate the shape and structure of NumPy arrays without changing the underlying data.

---

## 📚 Topics Covered

- `reshape()`
- `flatten()`
- `ravel()`
- `transpose()`
- `.T`
- Changing array dimensions
- Copy vs View
- Array structure transformation

---

## 1. reshape()

`reshape()` changes the shape of an array while keeping the same elements.

```python
import numpy as np

arr = np.arange(1,13)

arr2 = arr.reshape(3,4)

print(arr2)
```

Output:

```text
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
```

### Important Rule

The total number of elements must remain the same.

For an array containing 12 elements:

```text
3 × 4 = 12
4 × 3 = 12
2 × 6 = 12
```

All are valid reshapes.

---

## 2. flatten()

`flatten()` converts a multidimensional array into a 1D array.

```python
arr = np.array([
    [10,20,30],
    [40,50,60]
])

flat = arr.flatten()

print(flat)
```

Output:

```text
[10 20 30 40 50 60]
```

### Important

`flatten()` always returns a **copy**.

Therefore, changing the flattened array does not change the original array.

---

## 3. ravel()

`ravel()` also converts an array into a 1D array.

```python
r = arr.ravel()
```

### Important Difference

```text
flatten() → always returns a copy
ravel()   → returns a view when possible
```

Because `ravel()` can avoid creating a copy, it can be more memory-efficient.

---

## 4. transpose()

Transpose swaps rows and columns.

```python
arr = np.array([
    [10,20,30],
    [40,50,60]
])

print(arr.T)
```

Output:

```text
[[10 40]
 [20 50]
 [30 60]]
```

The shape changes:

```text
(2,3) → (3,2)
```

`arr.T` and `arr.transpose()` can be used for a 2D array to obtain the transpose.

---

## 🔄 Combining Array Manipulation

```python
data = np.arange(1,13)

matrix = data.reshape(3,4)

print(matrix)

print(matrix.T)

print(matrix.flatten())

print(matrix.ravel())
```

This demonstrates multiple array manipulation techniques together.

---

## 💡 Key Learnings

- `reshape()` changes array shape.
- The number of elements must remain unchanged when reshaping.
- `flatten()` converts an array to 1D and creates a copy.
- `ravel()` converts an array to 1D and returns a view when possible.
- `transpose()` swaps rows and columns.
- `.T` provides the transpose of an array.
- Array manipulation is useful when transforming data for different processing operations.

---

## 🎯 Interview Questions

### What is reshape?

`reshape()` changes the shape of an array without changing its data.

### What is the difference between flatten and ravel?

`flatten()` always creates a copy, while `ravel()` returns a view when possible.

### What does transpose do?

Transpose swaps rows and columns of a multidimensional array.

### What happens if the reshape dimensions don't match the number of elements?

NumPy raises an error because the total number of elements must remain the same.

---

## 📈 NumPy Progress

- ✅ Day 31 - NumPy Fundamentals
- ✅ Day 32 - Array Creation
- ✅ Day 33 - Mathematical Operations
- ✅ Day 34 - Boolean Indexing & Filtering
- ✅ Day 35 - Random Module
- ✅ Day 36 - Broadcasting
- ✅ Day 37 - Array Manipulation
- ⏳ Day 38 - Stacking & Splitting
- ⏳ Day 39 - Advanced Indexing
- ⏳ Day 40 - NumPy Mini Project

---

## 💻 Technologies Used

- Python
- NumPy
- Jupyter Notebook
- Git & GitHub
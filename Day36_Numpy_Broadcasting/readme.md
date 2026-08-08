# Day 36 - NumPy Broadcasting

## 📖 Overview

Today I learned about NumPy broadcasting and how NumPy performs arithmetic operations between arrays without explicitly writing loops.

---

## 📚 Topics Covered

- Broadcasting
- Vectorized Operations
- Scalar Broadcasting
- Broadcasting with 1D Arrays
- Broadcasting with 2D Arrays
- Broadcasting Rules
- Compatible and Incompatible Shapes
- Broadcasting Errors

---

## 🛠 Concepts Practiced

### 1. Scalar Broadcasting

```python
arr = np.array([10,20,30,40])

print(arr + 5)
print(arr * 3)
```

NumPy applies the scalar operation to every element.

---

### 2. Broadcasting with 2D Arrays

```python
arr = np.array([
    [10,20,30],
    [40,50,60]
])

print(arr + 5)
```

The scalar is broadcast across the entire array.

---

### 3. Broadcasting with 1D Arrays

```python
arr = np.array([
    [10,20,30],
    [40,50,60]
])

values = np.array([1,2,3])

print(arr + values)
```

Output:

```text
[[11 22 33]
 [41 52 63]]
```

---

### 4. Broadcasting with `(2,1)` and `(3,)`

```python
a = np.array([
    [10],
    [20]
])

b = np.array([100,200,300])

print(a + b)
```

Output:

```text
[[110 210 310]
 [120 220 320]]
```

---

## 💡 Broadcasting Rules

NumPy compares array dimensions from **right to left**.

Two dimensions are compatible when:

1. They are equal, OR
2. One of them is `1`.

Examples:

```text
(2,3) and (3,)     → Compatible
(2,1) and (3,)     → Compatible
(2,3) and (1,3)    → Compatible
(2,3) and (2,)     → Not Compatible
```

---

## 🎯 Key Learnings

- Broadcasting allows arithmetic operations between compatible arrays.
- Broadcasting avoids the need for explicit loops.
- NumPy performs operations using vectorization.
- Scalar values can be broadcast across arrays.
- Array dimensions are compared from right to left.
- Dimensions must either match or one dimension must be `1`.

---

## 🌍 Real-World Data Engineering Example

Broadcasting can be used for numerical transformations such as applying discounts, taxes, adjustments, or other calculations to datasets.

Example:

```python
sales = np.array([
    [100,200,300],
    [400,500,600]
])

discount = np.array([10,20,30])

final_sales = sales - discount

print(final_sales)
```

Output:

```text
[[ 90 180 270]
 [390 480 570]]
```

---

## 🎯 Interview Concepts

- What is NumPy broadcasting?
- Why does NumPy support broadcasting?
- What are the broadcasting rules?
- Why does `(2,3)` work with `(3,)`?
- Why does `(2,3)` fail with `(2,)`?
- Difference between broadcasting and explicit loops.

---

## 📈 Progress

- ✅ Day 31 - NumPy Fundamentals
- ✅ Day 32 - Array Creation
- ✅ Day 33 - Mathematical Operations
- ✅ Day 34 - Boolean Indexing & Filtering
- ✅ Day 35 - Random Module
- ✅ Day 36 - Broadcasting
- ⏳ Next: Day 37 - Array Manipulation

---

## 💻 Technologies Used

- Python
- NumPy
- Jupyter Notebook
- Git & GitHub
# Day 40 - NumPy Employee Analytics Project

## 📖 Project Overview

This project is the final project of my 10-day NumPy learning journey.

The project simulates a small Data Engineering-style employee data processing pipeline using NumPy.

The objective was to take employee data, perform filtering and transformation, process the data in batches, and finally generate useful business analytics.

---

## 🛠️ Technologies Used

- Python
- NumPy
- Jupyter Notebook
- Git
- GitHub

---

## 📊 Dataset

The employee dataset contains 10 employees with 4 columns:

| Column | Description |
|---|---|
| Employee ID | Unique employee identifier |
| Salary | Annual salary |
| Experience | Years of experience |
| Performance | Employee performance score |

Example:

```python
employees = np.array([
    [101, 50000, 2, 78],
    [102, 75000, 4, 91],
    [103, 45000, 1, 65],
    [104, 90000, 6, 95],
    [105, 60000, 3, 82],
    [106, 40000, 1, 58],
    [107, 85000, 5, 88],
    [108, 55000, 2, 72],
    [109, 95000, 7, 97],
    [110, 70000, 4, 85]
])
```

---

# 🚀 Project Stages

## Stage 1 - Dataset Creation & Basic Analysis

Performed:

- Created NumPy employee dataset
- Checked dataset shape
- Counted employees and columns
- Selected employee IDs
- Selected salary column
- Selected performance column
- Calculated salary statistics
- Calculated average performance

Important NumPy concepts:

```python
employees.shape
employees[:,0]
employees[:,1]
employees[:,3]

np.mean()
np.max()
np.min()
```

---

## Stage 2 - Filtering & Analytics

Filtered employees based on:

- Salary
- Performance
- Experience
- Multiple conditions

Example:

```python
high_salary = employees[employees[:,1] > 70000]
```

Multiple conditions:

```python
high_salary_performance = employees[
    (employees[:,1] > 70000) &
    (employees[:,3] >= 85)
]
```

Also used `np.where()` for classification.

---

## Stage 3 - Data Transformation

Created salary classifications:

```python
salary_status = np.where(
    salary >= 70000,
    "High",
    "Normal"
)
```

Created performance classifications:

```python
performance_status = np.where(
    employees[:,3] >= 85,
    "Excellent",
    "Average"
)
```

Calculated the number of excellent performers:

```python
excellent_count = np.sum(
    employees[:,3] >= 85
)
```

Found the highest-performing employee:

```python
max_performance = np.max(employees[:,3])

best_employee_index = np.where(
    employees[:,3] == max_performance
)[0]

best_employee = employees[best_employee_index]
```

---

## Stage 4 - Batch Processing

The employee dataset was divided into batches using:

```python
batches = np.array_split(employees, 3)
```

The batches were then processed individually.

For every batch, calculated:

- Number of employees
- Average salary
- Average performance
- Highest performance

Example:

```python
for i, batch in enumerate(batches):

    employee_count = batch.shape[0]
    avg_salary = np.mean(batch[:,1])
    avg_performance = np.mean(batch[:,3])
    highest_performance = np.max(batch[:,3])
```

A final batch report was created:

```python
batch_report = []

for i, batch in enumerate(batches):

    employee_count = batch.shape[0]
    avg_salary = np.mean(batch[:,1])
    avg_performance = np.mean(batch[:,3])
    highest_performance = np.max(batch[:,3])

    row = [
        i + 1,
        employee_count,
        avg_salary,
        avg_performance,
        highest_performance
    ]

    batch_report.append(row)

batch_report = np.array(batch_report)
```

Final report shape:

```text
(3, 5)
```

---

# Stage 5 - Final Analytics

The final stage answered important business questions.

## Overall Average Salary

```python
overall_avg_salary = np.mean(employees[:,1])
```

Result:

```text
66500.0
```

## Overall Average Performance

```python
overall_avg_performance = np.mean(employees[:,3])
```

Result:

```text
81.1
```

## Excellent Employees

```python
excellent_count = np.sum(
    employees[:,3] >= 85
)
```

Result:

```text
5
```

## Excellent Employee Percentage

```python
percentage = (
    excellent_count / employees.shape[0]
) * 100
```

Result:

```text
50.0%
```

## Best Employee

```python
max_performance = np.max(employees[:,3])

best_employee_index = np.where(
    employees[:,3] == max_performance
)[0]

best_employee = employees[best_employee_index]
```

Result:

```text
[[109 95000 7 97]]
```

Therefore:

```text
Employee ID: 109
Salary: 95000
Experience: 7 years
Performance: 97
```

---

# 📈 Batch Results

| Batch | Employees | Average Salary | Average Performance | Highest Performance |
|---|---:|---:|---:|---:|
| 1 | 4 | 65000.00 | 82.25 | 95 |
| 2 | 3 | 61666.67 | 76.00 | 88 |
| 3 | 3 | 73333.33 | 84.67 | 97 |

---

# 💡 Business Insights

### 1. Overall Salary

The average salary of all employees is:

```text
₹66,500
```

### 2. Overall Performance

The average performance score is:

```text
81.1
```

### 3. Excellent Performers

5 out of 10 employees have a performance score of at least 85.

Therefore:

```text
50% of employees are excellent performers.
```

### 4. Best Employee

Employee 109 has the highest performance score:

```text
Performance: 97
Salary: ₹95,000
Experience: 7 years
```

### 5. Best Batch

Batch 3 has the highest average salary:

```text
₹73,333.33
```

Batch 3 also has the highest average performance:

```text
84.67
```

Batch 3 contains the highest-performing employee with a score of:

```text
97
```

---

# 🧠 NumPy Concepts Used

During this project I practiced:

- `np.array()`
- `np.zeros()`
- `np.ones()`
- `np.full()`
- `np.arange()`
- `np.linspace()`
- `np.eye()`
- `.shape`
- `.reshape()`
- `.flatten()`
- `.ravel()`
- `.T`
- `np.sum()`
- `np.mean()`
- `np.min()`
- `np.max()`
- `np.std()`
- `np.var()`
- Axis operations
- Boolean indexing
- Advanced/Fancy indexing
- Broadcasting
- `np.random`
- `np.concatenate()`
- `np.vstack()`
- `np.hstack()`
- `np.split()`
- `np.array_split()`
- `np.where()`

---

# 🔄 Data Processing Pipeline

The complete project workflow was:

```text
Employee Dataset
       ↓
NumPy Array
       ↓
Inspect Dataset
       ↓
Select Columns
       ↓
Calculate Statistics
       ↓
Filter Employees
       ↓
Apply Multiple Conditions
       ↓
Classify Employees
       ↓
Find Best Employee
       ↓
Split Data into Batches
       ↓
Process Each Batch
       ↓
Create Batch Report
       ↓
Final Analytics
       ↓
Business Insights
```

---

# 🎯 What I Learned

Through this project I learned how NumPy can be used to:

- Store structured numerical data
- Select rows and columns
- Filter data using conditions
- Perform vectorized calculations
- Transform data using conditions
- Process data in batches
- Calculate statistics
- Generate analytical reports

This project helped me understand how NumPy can be used as a foundation for data processing and Data Engineering workflows.

---

# 📁 Project Structure

```text
Day40_NumPy_Employee_Analytics/
│
├── NumPy_Employee_Analytics.ipynb
│
└── README.md
```

---

# 📈 Learning Progress

- ✅ Day 31 - NumPy Fundamentals
- ✅ Day 32 - Array Creation
- ✅ Day 33 - NumPy Mathematical Operations
- ✅ Day 34 - Boolean Indexing & Filtering
- ✅ Day 35 - NumPy Random Module
- ✅ Day 36 - Broadcasting
- ✅ Day 37 - Array Manipulation
- ✅ Day 38 - Stacking & Splitting
- ✅ Day 39 - Advanced Indexing
- ✅ Day 40 - NumPy Employee Analytics Project

---

# 🏆 Project Status

**Completed ✅**

NumPy learning journey completed from Day 31 to Day 40.

Next step:

```text
NumPy ✅
   ↓
Pandas 🚀
   ↓
Data Cleaning
   ↓
Data Analysis
   ↓
Data Engineering Projects
```
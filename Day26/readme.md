# Day 26 - Python CSV Module & Sales Report Generator

## 📖 Overview

Today I learned how to work with CSV files using Python's built-in `csv` module. I explored both reading and writing CSV files using list-based and dictionary-based approaches.

To apply these concepts, I built a **Sales Report Generator** that reads sales data from a CSV file, calculates revenue for each product, and computes the total revenue.

---

## 📚 Concepts Covered

- `csv.reader()`
- `csv.DictReader()`
- `csv.writer()`
- `csv.DictWriter()`
- `next()`
- `writeheader()`
- `writerow()`
- Reading CSV files
- Writing CSV files
- Type Conversion (`int()`)
- Revenue Calculation
- Running Total using `+=`

---

## 🛠️ Mini Project - Sales Report Generator

### Features

- Reads sales data from a CSV file.
- Uses `csv.DictReader()` to access data by column names.
- Calculates revenue for each product using:

```
Revenue = Quantity × Price
```

- Displays product-wise revenue.
- Calculates and prints the total revenue.

---

## 📂 Input File (`sales.csv`)

```csv
Product,Quantity,Price
Laptop,2,50000
Mouse,5,800
Keyboard,3,1500
Monitor,2,12000
```

---

## 📤 Sample Output

```text
Laptop -> 100000
Mouse -> 4000
Keyboard -> 4500
Monitor -> 24000

Total Revenue = 132500
```

---

## 💡 Key Learnings

- CSV files store data as plain text.
- `csv.reader()` returns each row as a list.
- `csv.DictReader()` returns each row as a dictionary.
- `csv.writer()` writes data using lists.
- `csv.DictWriter()` writes data using dictionaries.
- Values read from a CSV file are strings by default.
- Numeric values must be converted before performing calculations.
- Running totals should be initialized **before** the loop.

---

## 📈 Skills Improved

- Python CSV File Handling
- Data Processing
- Dictionary Handling
- Type Conversion
- Looping Through Data
- Running Totals
- ETL Fundamentals

---

## 🎯 Project Outcome

Successfully built a Sales Report Generator that processes CSV data, calculates revenue for each product, and generates the total revenue automatically.

---

## 📌 Git Commit

```
Day 26: Learned CSV file handling and built a Sales Report Generator
```

---

## 🚀 Next Goal

Learn Python Exception Handling (`try`, `except`, `else`, `finally`, and `raise`) to build robust ETL pipelines that can safely handle invalid or missing data.
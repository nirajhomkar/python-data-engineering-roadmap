# Day 30 - Mini ETL Pipeline (Python for Data Engineering)

## 📖 Project Overview

Built a complete ETL (Extract, Transform, Load) pipeline using Python.

---

## 🚀 Features

### Extract
- Read configuration from JSON.
- Read sales data from CSV.

### Transform
- Calculated revenue for each product.
- Stored transformed data in memory.

### Load
- Generated processed_sales.csv.
- Generated summary.json.

### Backup
- Created backup of original sales file.
- Created ZIP archive of backup.

### Archive
- Moved processed input file to archive folder.

### Logging
- Logged every ETL step.
- Logged errors using logging.exception().
- Logged successful completion.

---

## 📚 Concepts Used

- CSV
- JSON
- Logging
- Exception Handling
- shutil
- ETL Design
- File Handling

---

## 📈 Skills Learned

- Extracting data from multiple sources.
- Transforming business data.
- Loading processed data into new files.
- Creating summaries.
- Managing backups.
- Production-style logging.
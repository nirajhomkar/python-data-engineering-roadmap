# Day 29 - Python Logging Module

## 📖 Overview

Today I learned how to use Python's built-in `logging` module to record application events, warnings, and errors. Logging is essential for monitoring and debugging production applications and ETL pipelines.

---

## 📚 Topics Covered

- logging module
- logging.basicConfig()
- Log Levels
  - DEBUG
  - INFO
  - WARNING
  - ERROR
  - CRITICAL
- Logging to a file
- Log formatting
- logging.exception()
- try-except-finally with logging

---

## 🛠 Mini Project - ETL Logger

### Features

- Logs application start.
- Logs file reading.
- Logs processing completion.
- Logs exceptions with traceback.
- Logs program completion.

---

## 💡 Key Learnings

- Logging is preferred over print statements in production.
- Log files help debug applications after execution.
- `logging.exception()` records both the error message and traceback.
- `finally` is the ideal place to log program completion.

---

## 📈 Skills Improved

- Production Logging
- Error Handling
- ETL Monitoring
- Debugging
- Python Automation
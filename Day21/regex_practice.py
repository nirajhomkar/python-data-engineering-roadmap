import re

# ----------------------------------------
# 1. re.search()
# ----------------------------------------

text = "Python is easy to learn"

result = re.search("Python", text)

print("1. re.search()")
print(result)
print(result is None)
print()

# ----------------------------------------
# 2. re.findall()
# ----------------------------------------

text = "Java Python C++ Python Java Python"

result = re.findall("Python", text)

print("2. re.findall()")
print(f"Matches : {result}")
print(f"Count   : {len(result)}")
print()

# ----------------------------------------
# 3. Extract Phone Numbers
# ----------------------------------------

text = """
Niraj : 9876543210
Rahul : 9988776655
Amit  : 9123456789
"""

result = re.findall(r"\d{10}", text)

print("3. Phone Numbers")
print(f"Phone Numbers : {result}")
print(f"Total Numbers : {len(result)}")
print()

# ----------------------------------------
# 4. Extract Email Addresses
# ----------------------------------------

text = """
Name: Niraj
Email: niraj@gmail.com

Name: Rahul
Email: rahul123@yahoo.com

Name: Amit
Email: amit@test.org
"""

result = re.findall(r"\w+@\w+\.\w+", text)

print("4. Email Addresses")
print(f"Emails Found : {result}")
print(f"Total Emails : {len(result)}")
print()

# ----------------------------------------
# 5. Extract Numbers using \d+
# ----------------------------------------

text = "Age: 25, Marks: 98, Roll: 101"

result = re.findall(r"\d+", text)

print("5. Numbers")
print(result)
print()

# ----------------------------------------
# 6. Uppercase Letters
# ----------------------------------------

text = "JavaPythonSQLAWS123"

result = re.findall(r"[A-Z]", text)

print("6. Uppercase Letters")
print(f"Uppercase Letters : {result}")
print(f"Count             : {len(result)}")
print()

# ----------------------------------------
# 7. Lowercase Letters
# ----------------------------------------

result = re.findall(r"[a-z]", text)

print("7. Lowercase Letters")
print(result)
print()

# ----------------------------------------
# 8. Characters Except Digits
# ----------------------------------------

text = "ABC123xyz"

result = re.findall(r"[^0-9]", text)

print("8. Not Digits")
print(result)
print()

# ----------------------------------------
# 9. Starts With (^)
# ----------------------------------------

text = "Hello Niraj"

result = re.search(r"^Hello", text)

print("9. Starts With")
print(result)
print(result is None)
print()

# ----------------------------------------
# 10. Ends With ($)
# ----------------------------------------

text = "niraj@gmail.com"

result = re.search(r"com$", text)

print("10. Ends With")
print(result)
print(result is None)
print()
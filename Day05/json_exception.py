"""
Day 5 - Exception Handling & JSON

Author: Niraj Homkar

Topics Covered:
1. try
2. except
3. else
4. finally
5. JSON Object
6. json.dumps()
7. json.loads()
8. JSON Array
"""

import json

# ----------------------------------------
# Exception Handling
# ----------------------------------------

print("=" * 40)
print("Exception Handling")
print("=" * 40)

a = 20
b = 5

try:
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result = {result}")
finally:
    print("Program Executed Successfully")

# ----------------------------------------
# JSON Object
# ----------------------------------------

print("\n" + "=" * 40)
print("Python Dictionary to JSON")
print("=" * 40)

employee = {
    "name": "Niraj",
    "salary": 60000,
    "city": "Bangalore"
}

json_data = json.dumps(employee)

print(json_data)

# ----------------------------------------
# JSON String to Dictionary
# ----------------------------------------

print("\n" + "=" * 40)
print("JSON to Dictionary")
print("=" * 40)

json_string = '{"name":"Rahul","salary":55000,"city":"Pune"}'

employee = json.loads(json_string)

print(f"{employee['name']} lives in {employee['city']}")

# ----------------------------------------
# JSON Array
# ----------------------------------------

print("\n" + "=" * 40)
print("JSON Array")
print("=" * 40)

json_array = '''
[
    {"name":"Niraj","salary":60000},
    {"name":"Rahul","salary":55000},
    {"name":"Amit","salary":70000},
    {"name":"Ravi","salary":65000}
]
'''

employees = json.loads(json_array)

for employee in employees:
    if employee["salary"] > 60000:
        print(f"{employee['name']} earns ₹{employee['salary']}")

print("\nDay 5 Completed Successfully!")
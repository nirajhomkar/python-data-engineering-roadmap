import json

employee = {
    "name": "Amit",
    "salary": 50000,
    "department": "IT"
}

with open("employee.json", "w") as file:
    json.dump(employee, file)

print("JSON file created successfully.")
import json
with open("employees.json","r") as file:
    data = json.load(file)
    for employee in data:
        print(f"ID: {employee['id']}\n Name: {employee['name']}\n Department: {employee['department']}\n Salary: {employee['salary']}\n")
    new_employee = {
    "id": 3,
    "name": "Amit",
    "department": "Finance",
    "salary": 55000
}
    data.append(new_employee)

with open("employees.json","w") as file2:
   
    json.dump(data, file2)
    print("New employee added successfully.")
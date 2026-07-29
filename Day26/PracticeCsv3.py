import csv

with open("employees2.csv","w",newline="") as file:
    field=["Name", "Salary", "Department"]
    writer = csv.DictWriter(file, fieldnames=field)
    writer.writeheader()
    writer.writerow({"Name": "Rahul", "Salary": 50000, "Department": "IT"})
    writer.writerow({"Name": "Priya", "Salary": 60000, "Department": "HR"})
    writer.writerow({"Name": "Amit", "Salary": 45000, "Department": "Finance"})
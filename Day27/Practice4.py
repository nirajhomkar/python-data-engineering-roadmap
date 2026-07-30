import json

with open("employee.json", "r") as file:
    data = json.load(file)
    print(data)
    print(type(data))
    print(data['department'])
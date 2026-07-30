import json

student = {
    "name": "Niraj",
    "age": 22,
    "city": "Bangalore"
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data))
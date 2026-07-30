import json

json_data = '{"name":"Rahul","age":23,"city":"Pune"}'

data = json.loads(json_data)

print(data)
print(type(data))

print(data["city"])
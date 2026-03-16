import json

json_string = '{"name": "Musa", "age": 23, "city": "Lagos"}'
# Deserialize the JSON string back into a Python object
data = json.loads(json_string)

# Or read from a file and deserialize
with open('data.json', 'r') as file:
    data = json.load(file)
print(data)
import json

def process_json(data: dict, filename: str) -> dict:

#Tried my best to serialize it even if i looked at my previous example
    with open(filename, 'w') as file:
        json.dump(data, file)

#Deserialization
    with open(filename, 'r') as file:
        python_dict =  json.load(file)
        return python_dict


data = {
    'name': "Musa",
    'age': 23,
    'city': 'Lagos'
        }

print(process_json(data, 'test.json'))


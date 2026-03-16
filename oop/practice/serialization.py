# import json 

# data = {'name': "Musa", 'age': 23, 'city': 'Lagos'}
# json_string = json.dumps(data)

# with open('data.json', 'w') as file:
#     json.dump(data, file)



import json

data = {
    'name': "Musa",
    'age': 23,
    'city': 'Lagos'
        }

json_string = json.dumps(data)

with open('data.json', 'w') as file:
    json.dump(data, file)   


import pickle

#Sample Python object
data = {'name': 'Alice', 'age': 23, 'city': 'Lagos'}

#Serialize the object to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)



# Deserialize the object from the file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data)
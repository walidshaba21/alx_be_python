# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         return "Woof"
    

# dog1 = Dog('Buddy', 'Golden Retriever')
# dog2 = Dog('Max', 'German Shephard')

# print(f"{dog1.name} is a {dog1.breed}. He says {dog1.bark()}")

# print(f"{dog2.name} is a {dog1.breed}. He says {dog2.bark()}")



class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Hiii!!")



class Lion(Animal):
    def speak(self):
        return f"{self.name} the lion roars"
    
class Elephant(Animal):
    def speak(self):
        return f"{self.name} the elephant trumpets"
    

#Polymorphism

zoo = [
    Lion('Simba'),
    Elephant("Dumbo")
]


for animal in zoo:
    print(animal.speak())
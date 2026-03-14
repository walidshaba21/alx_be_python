# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Hello my name is {self.name} and i am {self.age}"
    
#     def __del__(self):
#         print(f"Yeah {self.name} obj is being deleted")
    

# musa  = Person("Musa", 23)

# print(musa)


# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def  __repr__(self):
#         return f"Book (Title={self.title}, Author={self.author}, Pages={self.pages})"
        
#     def __str__(self):
#         return f"{self.title} was written by {self.author} with {self.pages} pages"
    
    

# mybook = Book("Python", "Musa Shaba", 200)

# print(mybook)
# print(repr(mybook))




class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name}, is munching generally like an animal"
    
    def sleep(self):
        return f"{self.name}, is snoozing generally like an animal"
    
class Dog(Animal):
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name}, is munching like a dog"
    
    def sleep(self):
        return f"{self.name}, is snoozing like a dog"
    
    def bark(self):
        return "Woof Woof!!"

animal = Animal("crab")
dog = Dog("Bingo")

tsk = [animal, dog]

for obj in tsk:
    print(f"{obj.eat()} \n{obj.sleep()}" )

    if isinstance(obj, Dog):
        print(obj.bark())

    print()



# class Book:
#     total_books = 0 
     
#     def __init__(self, name):
#         self.name = name
#         Book.total_books += 1

        
#     @classmethod
#     def display_total_books(cls):
#         print(f"Total books: {cls.total_books}")




# book1 = Book("How to write python")
# book2 = Book("Just for test")

# Book.display_total_books()


# class Calculator:

#     @staticmethod
#     def add(a, b):
#         return(a + b)
    
#     @staticmethod
#     def multiply(a, b):
#         return(a * b)

# print(Calculator.add(5, 6))
# print(Calculator.multiply(5, 6))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_child(cls, name):
        return cls(name, 0)
    
child = Person.create_child("Ali")
print(child.name)
print(child.age)

        
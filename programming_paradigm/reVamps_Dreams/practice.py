# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age =age

#     def student_info(self):
#         return f"{self.name} is {self.age}"


# student1 = Student('Musa', 23)

# print(student1.student_info())


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_product_value(self):
        value = self.price * self.quantity
        return f"The Total value of {self.name} is {value}"
    

product1 = Product("Apple", 500, 30)

print(product1.total_product_value())

    

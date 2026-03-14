# class Shape:
#     def calculate_area(self):
#         pass


# class Rectangle(Shape): 
#     def __init__(self, lenght, width):
#         self.length = lenght
#         self.width = width
#     def calculate_area(self):
#         return self.length * self.width
    

# rectangle = Rectangle(5,10)
# print(f"Area of rectangle: {rectangle.calculate_area()}")



# class Bird:
#     def fly(self):
#         return "Flying..."
    
# class Mammal:
#     def run(self):
#         return "Running..."
    

# class Bat(Bird, Mammal):
#     def fly(self):
#         return "Bat is flying"

#     def run(self):
#         return "Bat is running"


# bat = Bat()

# print(bat.fly())
# print(bat.run())        



class Dog:
    def make_sound(self):
        return("Dog is Barking!!!")

class Cat:
    def make_sound(self):
        return("Cat is Meowing!!!")

class Bird:
    def make_sound(self):
        return("Bird is chirping!!!")



def let_them_speak(animal):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Bird()]

let_them_speak(animals)
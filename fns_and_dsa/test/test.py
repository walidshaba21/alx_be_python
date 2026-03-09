import random

numbers = [random.randint(1, 10) for num in range(15)]

unique_numbers = set(numbers)

print("Unique numbers:", unique_numbers)


list = ["i am 1 ", "I am 2", " I am 3", "I am 4"]

tuple = (10, 20, 30)

diction = {
    "name": "Musa",
    "age": 23,
    "grade": "A"
}

num = {1,2,3,4}

person = ("John", 25)
print(person[0])

person += ("USA", )
print(person)
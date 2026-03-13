# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
    
#     result = num1 / num2
#     print(result)
# except ZeroDivisionError:
#     print("Can't Divide by Zero")


# file = input("Enter a file: ")
# try:
#     f = open(file)
# except FileNotFoundError:
#     print("Check Again file doesn't exist")

# else:
#     print(f.read())
#     f.close()



# class ValueTooHighError(Exception):
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return "The Value {} is greater than 100".format(self.value)




# try:
#     number = int(input("Enter a value not greater than 100: "))
#     if number > 100:
#         raise ValueTooHighError(number)
# except ValueTooHighError as e:
#     print(e)
# else:
#     print("Great! The number is at range")


# ChatGPT simplified

class ValueTooHighError(Exception):
    pass

try:
    number = int(input("Enter a value not greater than 100: "))

    if number > 100:
        raise ValueTooHighError(f"The value {number} is greater than 100")
except ValueTooHighError as e:
    print(e)

else:
    print("Great! The number is in ranges")
# def divide(x, y):
#     if y == 0:
#         raise ZeroDivisionError("Division by zero isn't allowed")
#     return x / y


# try:
#     print(divide(5, 0))
# except ZeroDivisionError as e:
#     print(e)




# class OutofStockError(Exception):
#     def __init__(self, item_name):
#         self.item_name = item_name

#     def __str__(self):
#         return f"Sorry, the item '{self.item_name}' is out of stock."
        
# product_inventory = {
#     "apple": 10,
#     "banana": 5,
#     "orange": 0,
#     "grapes": 3
# }

# def purchase_item(item,  quantity):
#     try:
#         if product_inventory[item] == 0:
#             raise OutofStockError(item)
#         else:
#             print(f"Purchase successful: {quantity} {item}(s)")
#             product_inventory[item] -= quantity
#     except KeyError:
#         print(f"Sorry, '{item}' is not available in our inventory.  ")

# try:
#     purchase_item("watermelon", 1)
#     purchase_item("apple", 3)
#     purchase_item("orange", 1)
# except OutofStockError as e:
#     print(e)







try:
    f = open('test_file.txt')
    if f.name == 'corrupt_file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
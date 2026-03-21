# item1 = 'Phone'
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity

# print(type(item1))
# print(type(item1_price))
# print(type(item1_quantity))
# print(type(item1_price_total))

# Variable types display
import csv

class Item:
    pay_rate = 0.8 # The pay rate after 205 discount
    all = []
    def __init__(self, name: str, price: float, quantity =  0):
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero"
        #Assign to self object 
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = float(item.get('quantity')),
            )
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"



class Phone(Item):
    pass
    


phone1 = Phone("jscPhonev10", 500, 5)
phone1.broken_phones = 1
phone2 = Phone("jscPhonev20", 700, 5)
phone2.broken_phones = 1


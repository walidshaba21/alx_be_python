class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
            self.account_balance = self.account_balance + amount
            return f"{amount} has been deposited you new balance is {self.account_balance}"

    def withdraw(self, amount):
            if self.account_balance ==  0 or amount > self.account_balance:
                return False, "Inssuficient funds!"
            else:
                self.account_balance = self.account_balance - amount
                return True, f"${amount} withdrawn. New balance: ${self.account_balance}"

    def display_balance(self):
            print(f"Current Balance: {self.account_balance}.")


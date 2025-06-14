class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

        def deposit(self, amount):
            self.account_balance = self.account_balance + self.amount
            return f"{self.amount} has been deposited you new balance is {self.account_balance}"

        def withdraw(self, amount):
            if self.account_balance == 0:
                return "Your account balance is Zero! deposit an amount to be able to make withdrwal."
            elif self.amount > self.account_balance:
                return "Insufficient amount in you bank account to make withdraw!"
            else:
                self.account_balance = self.account_balance - self.amount
                return f"Your new account balance is {self.account_balance}, {self.amount} has been withdrawn."

        def display_balance(self):
            return f"Current Balance: {self.account_balance}."


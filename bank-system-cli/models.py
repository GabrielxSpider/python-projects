class User:
    def __init__(self, username, password, balance=0, history=None):
        self.username = username
        self.password = password
        self.balance = balance
        self.history = history if history else []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited {amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew {amount}")
            return True
        return False
    
    def to_dict(self):
        return {
            "password": self.password,
            "balance": self.balance,
            "history": self.history
        }
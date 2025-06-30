


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner         # public
        self._balance = balance    # protected
        self.__pin = 1234          # private

    def display(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self._balance}")
        print(f"PIN: {self.__pin}")  # Accessible within class

account = BankAccount("Alice", 1000)
account.display()

print(account.owner)       # Public - accessible
print(account._balance)    # Protected - accessible but not recommended
print(account.__pin)     # Error: Private attribute not directly accessible
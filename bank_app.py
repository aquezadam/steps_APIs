class BankAccount:
    def __init__(self, name, balance, account_num):
        self.name = name
        self.balance = balance
        self.account_num = account_num

    def display_balance(self):
        print(self.balance)

    def withdraw(self, withdraw_amount):
        if self.balance < withdraw_amount:
            print("Not enough balance")
        else:
            self.balance -= withdraw_amount

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

account_a = BankAccount("Ale", 1000, "AB5544")
account_a.display_balance()

account_a.deposit(3000)
account_a.display_balance()
account_a.withdraw(500)
account_a.display_balance()
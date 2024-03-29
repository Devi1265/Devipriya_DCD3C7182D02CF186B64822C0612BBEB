class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print("Deposited₹{}. New balance: {}".format(amount,self.__account_balance))
        else:
            print("Invalid deposit amount please deposit a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print("Withdraw ₹{}. New balance: {}".format(amount,self.__account_balance))
        else:
            print("Invalid withdrawal amount pr insufficient balance.")

    def display_balance(self):

      print("Account balance for{}(Account #{}:₹{}.".format(self.__account_holder_name,self.__account_number,self.__account_balance))
        

# create an instance of the Bank Account class 

account=BankAccount(account_number="1234567890",account_holder_name="devipriya",initial_balance=5000.0)

#Test deposit and withdrawal Functionally.

account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()
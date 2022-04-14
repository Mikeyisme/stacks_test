from codecs import BOM_BE


class User:
    def __init__(self, name, pin, password):

        self.name = name
        self.pin = pin
        self.password = password        

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password
        


#user1 = User("Bob", 1234, "password")
#print (user1.name, user1.pin, user1.password )


#user1 = User("Bob", 1234, "password")
#print (user1.name, user1.pin, user1.password)
#user1.change_name("Bobby")
#user1.change_pin(4321)
#user1.change_password("newpassword")
#print(user1.name, user1.pin, user1.password)

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "Has an account balance of", float(self.balance))

    def withdraw(self, withdraw_amount):
        self.balance = self.balance - withdraw_amount
        print(self.name, "Has an account balance of", self.balance)

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print(self.name, "Has an account balance of", self.balance)


#user1 = BankUser("Bob", 1234, "password")
#print (user1.name, user1.pin, user1.password, user1.balance)


# user1 = BankUser("Bob", 1234, "password")
# user1.show_balance()
# user1.deposit(1000.0)
# user1.show_balance()
# user1.withdraw(500.0)
# user1.show_balance()


    def transfer_money(self, amount, name):
        print("You are transferring $", amount, "to", name)
        print("Authentication Required")
        pin_input = input("Please enter your pin:")
        if int(pin_input) == self.pin:
            print("Transferring", amount, "to", name)
            self.balance = self.balance - amount
            name.balance = name.balance + amount
            print(self, "Has an account balance of", float(self.balance))
            print(name, "Has an account balance of", float(name.balance))
            return True
        else:
            print("Authentication Failed")
            return False
        
    def request_money(self, amount, name):
        print("You are requesting $", float(amount), "from", name)
        print("Authentication Required")
        their_pin_input = input("Please enter pin:")
        if int(their_pin_input) == name.pin:
            self.balance = self.balance + amount
            print("Requesting", amount, "from", name)
            request_amount = name.balance - amount
            name.balance = name.balance + request_amount
            print(self, "Has an account balance of", self.balance)
            print(name, "Has an account balance of", int(name.balance))
            return True
        else:
            print("Authentication Failed")
            return False

user1 = BankUser("Bob", 1234, "password")
user2 = BankUser("Ally", 5678, "allypassword")
user2.deposit(5000)
user2.show_balance()
user1.show_balance()
print()
transfer = user2.transfer_money(500, user1)
user2.show_balance()
user1.show_balance()
print()
# Week8 Day1 Lesson

class Dog:
    def __init__(self, color):  # created by default and called automatically when creating a new instance of the class
        print(f"creating dog instance with {color}")
        self.color = color  # self : this class => inside the class, I want to save attribute

    def bark(self):
        print("woof")


ricks0 = Dog('brown')  # create instance from the class dog
# ricks0.color = 'brown'  # create an attribute
print(ricks0.color)

# ricks1 = Dog()  # create instance from the class dog
# ricks1.color = 'black'


# => exception missing 1 required positional argument: 'color' if color is an attribute
# => exception Dog' object has no attribute 'color'

ricks1 = Dog("black")
print(ricks1.color)

# both expressions below are equivalent
ricks0.bark()
Dog.bark(ricks0)


class Point():
    def __init__(self, x, y):  # it is the constructor whose role is to initialize. It accepts 2 attributes.
        self.x = x  # self : this class => inside the class, the x attribute can be accessed
        self.y = y


## create an instance of the class
p = Point(3, 4)
p1 = Point(4, 12)

## access the attributes
print("p.x is:", p.x)
print("p.y is:", p.y)
print("p1.x is:", p1.x)
print("p1.y is:", p1.y)


class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print("{} barks ! WAF".format(self.name))


shelter_dog = Dog("Rex")  # shelter_dog is self
shelter_dog.bark()  # best practice
Dog.bark(shelter_dog)  # not a good practice


class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print("{} barks ! WAF".format(self.name))

    def walk(self, number_of_meters):
        print("{} walked {} meters".format(self.name, number_of_meters))

    def rename(self, new_name):
        self.name = new_name


shelter_dog = Dog("Rex")
print(f"before : {shelter_dog.name}")
shelter_dog.rename("Paul")
print(f"after : {shelter_dog.name}")


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Hello my name is " + self.name)

    def rename(self, new_name):
        self.name = new_name


first_person = Person("John", 36)
first_person.show_details()

print(f"before : {first_person.name}")
first_person.rename("Paul")
print(f"after : {first_person.name}")
first_person.show_details()

global counter
counter = 0

class Computer():
    def __init__(self):
        global counter
        counter += 1

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

    #def __str__(self):
        #return f"computer{self.name}" # will be seen later on

mac_computer = Computer()
mac_computer.brand = "Apple" # not a good practice to create here th attribute
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark") # a short way to call a function
# => same location in the memory

print(counter)

class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = [] # The user has not the ability at the beginning

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Successful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)

my_account = BankAccount(12)
my_account.view_balance()

your_account=BankAccount("1234",40)
your_account.view_balance()

my_account.deposit(amount=100)
my_account.view_balance()
withdraw_money = my_account.withdraw(60)
my_account.view_balance()

my_account.view_transactions()



myList = [10, 25, 17, 9, 30, -5]
# Double the value of each element
myList2 = map(lambda n : n*2, myList)
print(myList2)
# class methods ->  are methods that are not bound to an instance of a class but to a class itself.
# class methods can only access and modified class variables, and not instance variable.
# The first parameter of a class method is usually named cls, which refers to the class itself

# instance methods -> can access and modify both class and instance variables.
# Instance methods are defined with the def keyword within the class, and the first parameter is always self, which refers to the instance of the class.
# Inside instance methods, you can access and modify instance variables using self.
# Instance methods can also access and call other instance methods and class methods.

# static methods -> unlike instance and class methods, static methods can not access class attributes or instance attributes.
# In Python, we create static method using @staticmethod decorator.
# They are primarily used for utility functions that are related to the class but do not require access to instance or class data.
# They are similar to regular functions but are defined within a class for better organization and encapsulation.

class Account:
    minbalance = 1000 # class variable

    def __init__(self, name, accno, balance):
        self.name =name
        self.accno = accno
        self.balance = balance

    def display(self):
        print("Account Number: ", self.accno)
        print("Account Holder: ", self.name)
        print("Actual Balance: ", self.balance)

    def deposit(self, amt):
        self.balance = self.balance + amt
    
    @classmethod 
    def displayMin(cls):  # Account or cls (className)
        print("Minimum balance: ", Account.minbalance) # cls.minbalance
        # print('balance: ', cls.balance)
    
    @staticmethod 
    def checkBal(amt, bal):
        if(amt>bal):
            return -1
        else:
            return 1
    
    def withdraw(self, amt):
        r = Account.checkBal(amt,self.balance)
        if r==-1:
            print("Insufficient balance.")
        else:
            self.balance -= amt 
            print("amount withdrawl: ",self.balance)
a = Account("Suwas Ghale", 112233, 50000)
a.displayMin()
a.display()
a.deposit(5000)
a.display()

a.withdraw(20000)
a.withdraw(50000)


print("-----------Car--------------------")
class Car:
    wheels_num=4 # class variable.
    def __init__(self, brand, model, type, color):
        self.cbrand=brand,
        self.cmodel=model, # instance variable
        self.ctype =type,
        self.ccolor=color
    def display_car_info(self):
        print(f"Brand is: {self.cbrand} \n Model is: {self.cmodel}\n Type is: {self.ctype}\n Color is: {self.ccolor}")
    
    @classmethod
    def display_wheels(cls):
        print(f"The number of wheels is: {cls.wheels_num}")
    
    @staticmethod
    def honk():
        print("Beep! Beep!!")

# Creating instance of a car:
car1=Car("Lamborghini", 2024, "Electric", "Black")

# calling instance method
car1.display_car_info()

# calling static method
Car.honk()
car1.honk()

# calling class method
car1.display_wheels()
Car.display_wheels()


# instance method 
class Bike:
    def __init__(self,brand, model):
        self.bbrand = brand 
        self.bmodel = model
    def bike_info(self):
        print(f"Bike brand is: {self.bbrand} and model is: {self.bmodel}")

ns200=Bike('Pulsar', 2024)
ns200.bike_info()


# class method 
class Cow:
    legs=4
    def __init__(self, name, age) :
        self.cname=name
        self.cage=age 
    @classmethod 
    def display_legs(cls):
        print(f"The cow has {cls.legs} legs.")
        # print(f"The cow is {cls.cage} years old.")
jarsi=Cow("Jarsi",5)
jarsi.display_legs()

# staticmethod
class MathUtils:
    @staticmethod 
    def add(a,b):
        return a+b
    @staticmethod
    def multiply(a,b):
        return a*b

print(MathUtils.add(5,6))
print(MathUtils.multiply(5,6))
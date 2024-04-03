'''
Class Variables:
-> Class variables are variables that are shared among all instances of a class.
-> They are defined within the class but outside of any instance methods.
-> Class variables are accessed using the class name rather than through instances of the class.
-> They are typically used to store data that is common to all instances of the class.
-> Class variables are declared using the class name followed by the variable name, and are usually initialized within the class definition.


Instance Variables:
-> Instance variables are variables that are unique to each instance of a class.
-> They are defined within the constructor (__init__ method) using the self keyword, which refers to the instance of the class.
-> Each instance of the class has its own copy of instance variables, which can have different values.
-> Instance variables represent the state of each individual object created from the class.
-> Instance variables are accessed and modified using the instance name followed by the dot operator (.).


self in Python Class:
-> self represents the instance of the class.
-> By using 'self', we can access the attributes and methods of the class in Python.
-> self binds the attributes with the given arguments.
-> The first parameter of methods is the instance the method is called on.
'''

class Account:
    minbalance= 5000 # class variable - variable inside the class.

    def __init__(self, acc_no, name, balance) :
        self.acc_no= acc_no # instance variables - variable inside the method.
        self.name=name
        self.balance =balance
    
    def display(self):
        print("Account Number: ", self.acc_no)
        print("Account Holder: ", self.name)
        print("Actual Balance: ", self.balance)
        # print("Min Balance: ", self.minbalance)

obj_suwas = Account(157310011649,'Suwas Ghale', 15000000)
obj_samrat = Account(157310011655,'Samrat Lama', 1050000)

obj_suwas.display()
obj_samrat.display()

# print minbalance 
print("minmum balance: ", Account.minbalance)
print("minmum balance from obj_samrat: ", obj_samrat.minbalance)


class Car:
    wheels_num=4 # class variable.
    # The __init__ method is the constructor used to initialize new objects (instances) of the Car class.
    def __init__(self,brand, model, type):
        self.cbrand=brand # instance variable
        self.cmodel=model # instance variable
        self.ctype=type # instance variable
    def show(self):
        print(f"The car brand is: {self.cbrand}")
        print(f"The car model is: {self.cmodel}")
        print(f"The car type is: {self.ctype}")

car1=Car("Tesla", 2024, "Electric")
print(car1)
# accessing instance variables
# print(car1.cbrand) # instancename.instancevariable
# print(car1.cmodel)
# print(car1.ctype)
car1.show()
# accessing class variables
print(Car.wheels_num) # classname.classvariable
print(car1.wheels_num)
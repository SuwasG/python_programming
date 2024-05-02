# functions: a block of code to perform the particular task.
# The idea is to put some commonly or repeatedly done tasks together and make a functions so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.
# some benefits of using functions: Increase code Readablility and code Reusability.

def demo():
    print("Hello Suwas.")
demo()


# function with argument.
# Arguments are the values passed inside the parenthesis of the function.
# A function can have any number of arguments separated by a comma.
# pass the value when function is called
# define the function
def add(m,n):
    sum = m + n
#     print(f"sum of {m} and {n} is {sum}")
    print("sum of {} and {} is {}.".format(m,n,sum))
    

# call the function
add(20, 30)


# default argument -> a parameter that assumes a default value if a value is not provided in the function call for that argument.
def my_function(p, q=50):
    print("p: ", p)
    print("q: ", q)
my_function(25,45)
my_function(25)


# keyword argument -> to allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.
def employee(firstname, lastname):
    print(firstname, lastname)

employee(firstname="suwas", lastname='ghale')
employee(lastname="lama", firstname='sagar')


# positional argument
def bio(name,address, age):
    print("Hello, ", name)
    print("From: ", address)
    print("age: ", age)

bio("suwas", 'ktm', 22)
bio('suwas', 22,'rasuwa')



# arbitrary keyword arguments.
'''
In Python Arbitrary Keyword Arguments, *args and **kwargs can pass a variable number of arguments to a function using special symbols.
Ther are two special symbols:
1. *args in Python (Non-keyword arguments)
2. **kwargs in Python (keyword arguments)

'''
def myFun(*args):
    for ag in args:
        print(ag)
myFun("Hello", "Programming", "Suwas","Nepal")


def demoFun(**kwargs):
    for k,v in kwargs.items():
        print("%s == %s"%(k,v))

demoFun(name="Suwas", address="KTM", age='20', gender='male', isMarried=False, courses=['Python', 'JavaScript', 'PHP', 'Java', 'C'])

# function with return type
# define the function
def testFunction(a, b):
    sum = a*b
    return(f"multiply of {a} and {b} is {sum}")
# call the function
result = testFunction(5, 10)
result2= testFunction(8, 14)
print("result: ", result)
print("result2: ",result2)

# 
def is_prime(num):
    if num<=1:
        return False
    elif num==2:
        return True
    elif num%2==0:
        return False
    else:
        for i in range(3, int(num*0.5)+1,2):
            if num%i==0:
                return False
        return True

print(is_prime(35))


# Docstring: The first string after the function defined is called document string or docstring.
# Docstring is used to describe the functionality of the function and use is OPTIONAL but considered good practice.

def hello(name, address):
    "Function to introduce person."
    print("Hello, my name is: ", name)
    print("I am from: ", address)

hello("Suwas", 'Rasuwa')
print(hello.__doc__)
print(hello.__name__)


import math 
print("math.sqrt= ", int(math.sqrt(11))+1)
print(int(11*0.5)+1)
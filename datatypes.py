# Python inbuilt datatypes:
# Datatypes are the classification or categorization of data items.
# Datatype represents the kind of valu that tells what operations can be performed on a particular data.
# NOTE: Since everything is an OBJECT in Python programming, data types are classes and variables are instances(objects) of these classes.
# To define the value of various data types and check their data types, we use the type() function.

# intger (int): -> whole numbers 10,12, 19, 33, 89, 890
# float -> decimal numbers: 9.99, 87.99, 2.07, 2.00
# string (str) -> "Hello", 'hello' 
# list -> collection of datatypes. ['a','b','c'] mutable
# tuple -> ('a', 'b', 'c')   immutable
# dictionary (dict) -> {"key1":"value1", "Key2":"value2"}
# set -> unique elements. {10, 23,29, 28, 88}
# boolean -> true, false



# variables:  a container to store values or it can be called as data representation.

# Numeric data types in Python
x=12
print(x)

z= 2+5j
print(f"type of z is: {type(z)}") # <class 'complex'>
print("z is: {}".format(z))

# to check data type use, type()
print(type(x))


y=23.33
print(type(y))

z='66.67'
print(type(z))

from math import pi
print(pi)
print(type(pi))

# Sequence data type in Python
# string
name = "Suwas"
print("type of name is: {} ".format(type(name)))

# list
fruits=['orange', 'apple', 'banana', 'strawberry', 'pineapple']
print(fruits)
print("data type of fruits is: {}".format(type(fruits)))

# tuple -> collection of items.
colors=('yellow', 'red', 'blue', 'green', 'black', 'white', 'magenta', 'violet','amber')
print(colors)
print("data type of colors is: {}".format(type(colors)))

# dictionary
my_dictionary={
    "name":"Suwas",
    "address":"Rasuwa",
    "age":22,
    "language":"Python"
}

print(my_dictionary)
print("data type of my_dictionary is: {}".format(type(my_dictionary)))
print(my_dictionary.get("age"))
print(my_dictionary.get("ages"))
# print(my_dictionary['ages'])

# set -> unique element and random order.
s={1,2,2,5,8,3,9,5,3,4}
print(s)
print(type(s))

# boolean
a=True,
print(a)
print(type(a))

# bool -> True or False.
print(f"type of True is: {type(True)}")
print(f"type of False is: {type(False)}")

# challenge/practice
D = dict()
for x in enumerate(range(2)):
    D[x[0]]=x[1]
    D[x[1]+7] = x[0]
print(D)

g = {i:i*i for i in range(6)}
print(g)
'''
-> OOPs is a programming paradigm that uses Objects and Classes in programming.
-> It aims to implement real-world entities like Inheritance, Polymorphisms, Encapsulation, Abstractions , etc.
-> In the programming, the main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.

'''
# Class:
# Classes are created by using keyword 'Class'
# Class -> Class is the blueprint or template or the prototypes that defines the nature, attribute and methods of the future object.
# A Class is a collection of objects.
# Classes encapsulate data for the object and provide methods to operate on that data.
# They act as a user-defined data type in which we can define our own attributes and methods.
# Attributes are the variables that belong to a class.
# Attributes are always public and can be accessed using dot(.) operator. eg: MyClass.MyAttribute
# Classes facilitate code reusability and modularity by allowing similar objects to be created from the same blueprint.
# Modularity : focuses on separating functionality into independent modules or components.
# int is class and 10 is object.
print(type(10))
print(type("hello"))

class Student:
    pass

# define object
# object -> a variable created from the class.
# The objects are the basic building blocks of OOPs.
# An object is a self-contained entity that consists of both data/state (attributes) and procedures/behavior (methods) to manipulate that data.
# Objects represent real-world entities or concepts. For example, a car, a person, a bank account, etc.

ram = Student()
print(type(ram))


class Animal:
    pass

puppy = Animal()
print(type(puppy))

class Car:
    pass 
tesla=Car() # object creation from class.
#NOTE: The process of creating an object from a class is called instantiation. This involves allocating memory for the object and initializing its attributes.
print(type(tesla))
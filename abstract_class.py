# abstract classes are classes that contains one or more abstract methods.
# abstract method is a method that is declared but contains no implementations.
# Abstract class cannot be instantiated(can not make instance variables.) and require subclass to provode implementation for the abstract methods.
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(Polygon):
    def __init__(self, base, height):
        self.b= base 
        self.h= height
    def area(self):
      return  1/2*self.b * self.h

class Rectangle(Polygon):
    def __init__(self, l,b) :
        self.l = l
        self.b = b
    def area(self):
        return self.l*self.b

t = Triangle(3, 5)
print(t.area())

r = Rectangle(6,4)
print(r.area())
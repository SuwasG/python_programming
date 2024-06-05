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



class CoffeeMachine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def grind_beans(self):
        pass

    @abstractmethod
    def heat_water(self):
        pass

    @abstractmethod
    def brew_coffee(self):
        pass

    @abstractmethod
    def pour_coffee(self):
        pass

    def make_coffee(self):
        self.start()
        self.grind_beans()
        self.heat_water()
        self.brew_coffee()
        self.pour_coffee()


class SimpleCoffeeMachine(CoffeeMachine):
    def start(self):
        print("Starting the coffee machine...")

    def grind_beans(self):
        print("Grinding the coffee beans...")

    def heat_water(self):
        print("Heating the water...")

    def brew_coffee(self):
        print("Brewing the coffee...")

    def pour_coffee(self):
        print("Pouring the coffee into the cup...")

class AdvancedCoffeeMachine(CoffeeMachine):
    def start(self):
        print("Starting the advanced coffee machine with self-cleaning...")

    def grind_beans(self):
        print("Grinding the coffee beans with precision...")

    def heat_water(self):
        print("Heating the water to the optimal temperature...")

    def brew_coffee(self):
        print("Brewing the coffee with advanced techniques...")

    def pour_coffee(self):
        print("Pouring the coffee into the cup with perfect foam...")


def main():
    coffee_machine = SimpleCoffeeMachine()
    print("Using Simple Coffee Machine:")
    coffee_machine.make_coffee()

    print("\nUsing Advanced Coffee Machine:")
    advanced_coffee_machine = AdvancedCoffeeMachine()
    advanced_coffee_machine.make_coffee()

if __name__ == "__main__":
    main()


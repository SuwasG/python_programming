'''

Suppose you're designing a system for managing different types of vehicles in a transportation company. Vehicles include cars, trucks, and motorcycles. Each vehicle has common attributes such as make(company), model, year, and color, but they also have unique features and behaviors.

Design a Python program using inheritance to model this system. Implement a base class Vehicle with common attributes and methods, and derive subclasses Car, Truck, and Motorcycle that inherit from Vehicle. Each subclass should have its own unique attributes and methods specific to that type of vehicle.

Additionally, include methods in each subclass to perform vehicle-specific actions, such as drive for cars, load_cargo for trucks, and ride for motorcycles. Demonstrate the use of inheritance by creating instances of each subclass and invoking their methods.

'''

class Vehicle:
    def __init__(self, company,model,year, color):
        self.company=company
        self.model=model
        self.year=year 
        self.color=color
    
    def display_info(self):
        print(f"making company: {self.company}\n model: {self.model}\n year: {self.year}\n color: {self.color}.")

class Car(Vehicle):
    def __init__(self, company, model, year, color, payload_capacity):
        super().__init__(company, model, year, color)
        self.payload_capacity=payload_capacity

    def drive(self):
        print(f"{self.company} {self.model} Car is Driving.")

class Truck(Vehicle):
    def __init__(self, company, model, year, color, payload_capacity):
        super().__init__(company, model, year, color)
        self.payload_capacity=payload_capacity
    
    def load_cargo(self):
        print(f"Loading cargo into {self.company} {self.model} truck.")

class Motorcycle(Vehicle):
    def __init__(self, company, model, year, color, luggage_capacity):
        super().__init__(company, model, year, color)
        self.luggage_capacity=luggage_capacity
    
    def load_luggage(self):
        print(f"Loading luggage into {self.company} {self.model} motorbike.")

class ElectricCar(Car):
    def __init__(self, company, model, year, color,payload_capacity, battery_capacity):
        super().__init__(company, model, year, color, payload_capacity)
        self.battery_capacity=battery_capacity
    
    def charge(self):
        print(f"Charging {self.company} {self.model}'s battery.")

# Demonstration
car = Car("Toyota", "Camry", 2022, "Red", payload_capacity=4)
truck = Truck("Ford", "F-150", 2021, "Blue", payload_capacity=2000)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2020, "Black", luggage_capacity=300)
electric_car = ElectricCar("Tesla", "Model S", 2023, "White",4,  battery_capacity=100)

print("Car:")
car.display_info()
car.drive()

print("\nTruck:")
truck.display_info()
truck.load_cargo()

print("\nMotorcycle:")
motorcycle.display_info()
motorcycle.load_luggage()

print("\nElectric Car:")
electric_car.display_info()
electric_car.drive()
electric_car.charge()

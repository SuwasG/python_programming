# inheritance: is to form a new class from the parent class OR class that has been already defined. The newly formed class is known as derived class and class from which the new class is formed is known as base class.
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (subclass) to inherit attributes and methods from another class (superclass).
# In Python, inheritance is implemented using the syntax class SubClassName(SuperClassName)
class Animal:
    def __init__(self):
        print("Animal class created.")
    def who(self):
        print("Animal")
    def eat(self):
        print("Some animals are Carnivorous and Herbivorous.")
    def jump(self):
        print("Some animals can jump while some can't.")
    

class Dog(Animal):
    def who(self):
        print("Dog.")
    def sound(self):
        print("Bow Bow.")

class Lutre(Dog):
    def who(self):
        print("Lutre.")

# superclass: class with child class and subchild class.

obj_a= Animal()
print(obj_a)
obj_a.who()

obj_d= Dog()
obj_d.who()
obj_d.eat()
obj_d.jump()
obj_d.sound()

obj_l= Lutre()
print(type(obj_l))
obj_l.who()
obj_l.eat()
obj_l.jump()



'''
Consider a scenario where you're developing a system for managing employees in a company. You have different types of employees, such as full-time employees and part-time employees. Both types of employees have common attributes and behaviors, but they also have their own unique attributes and behaviors.
'''
class Employee:
    def __init__(self, emp_name, emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id 
    
    def employee_details(self):
        print(f"Employee Name: {self.emp_name}\nEmployee Id: {self.emp_id}")

class FullTimeEmployee(Employee):
    def __init__(self, emp_name, emp_id, salary):
        super().__init__(emp_name, emp_id)
        self.salary = salary
    
    def employee_details(self):
        super().employee_details()
        print(f"Salary: {self.salary}")

class PartTimeEmployee(Employee):
    def __init__(self, emp_name, emp_id, hourly_rate, hours_worked):
        super().__init__(emp_name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def employee_details(self):
        super().employee_details()
        print(f"Hourly Rate: ${self.hourly_rate}, Hours Worked: {self.hours_worked}")


full_time_emp = FullTimeEmployee("Ram", 55, 2000)
part_time_emp = PartTimeEmployee("Hari", 525, 20, 300)
full_time_emp.employee_details()
part_time_emp.employee_details()

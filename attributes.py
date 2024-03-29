# attributes -> properties of an object.
# attributes are pieces of data associated with a particular class or instance of a class.
# In Python, attributes are defined within a class and can be accessed using dot notation.

class Student:
    # method -> function defined inside the class
    # constructor -> if the function is automatically called
    def __init__(self, name, gender, address, years, text) :
        self.fullname = name  # fullname is attribute same like variable.
        self.gender = gender
        self.address = address
        self.age = years
        self.message = text
        

obj_suwas = Student("Suwas Ghale", "Male", "Kathmandu", 22, "Hello From Suwas")
# object ko direct value print garna namilney vayekale attribute bata garne.
print(obj_suwas.fullname)
print(obj_suwas.address)
print(obj_suwas.age)
print(obj_suwas.message)

obj_ram = Student("Ram Lama", "Male", "Pokhara", 23, "Hello from Ram, Good Luck")

print(obj_ram.fullname)
print(obj_ram.address)
print(obj_ram.age)
print(obj_ram.message)

print(type(obj_ram))
print(type(obj_ram.address))
print(type(obj_ram.age))


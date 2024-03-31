# methods: a function defined inside the body of the class.
# In Object-Oriented Programming (OOP), methods are functions that are defined within a class and are used to perform operations on the data (attributes) of the class.
# Method represents the behavior or actions that object of the class can perform.
# instance method, class method, and static methods.(explained on another file)


class Employee:
    def work(self):
        print("He is a Disk Jockey")

    def salary(self, pay):
        print("His salary is ", pay)

    def contactme(self, email, phone):
        print(f"His contact is\n email: {email} \n phone: {phone}")
    
   

obj_sujit = Employee()
obj_sujit.work()
obj_sujit.salary(77500)
obj_sujit.contactme('sujit@gmail.com', '9876487267')
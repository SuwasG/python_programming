# polymorphism: method overriding. same method can do different operations in different classes.

# The term polymorphism means many forms.

class Bird:
    def intro(self):
        print("There are many types of birds in the world.")
    
    def fly(self):
       print("Some birds can fly but some can not.")

# child class can extend or override the properties of parent class.

class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly.")

class Ostrich(Bird):
    def intro(self):
        print("Hello from Ostrich.")
    def fly(self):
        print("Ostrich can not fly.")

obj_bird= Bird()
obj_bird.intro()
obj_bird.fly()

obj_sparrow= Sparrow()
obj_sparrow.intro()
obj_sparrow.fly()

obj_ostrich = Ostrich()
obj_ostrich.intro()
obj_ostrich.fly()    
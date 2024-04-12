# methods can have same name and operations but parameter they take as input values are different.
#  a class can have multiple methods with the same name but different parameters.

class Student:
    def show(self, fname=None, lname=None):
        if fname is not None and lname is not None:
            print(f"hello {fname} {lname}.")
        elif fname is not None:
            print(f"hello {fname}.")
        else:
            print("hello")

obj_student = Student()
obj_student.show()
obj_student.show("Suwas")
obj_student.show("Suwas", "Ghale")


# Using default Parameter values.
class MathUtils:
    def add(self, x,y=5):
        print(f"{x}+ {y}={x+y}")

m1=MathUtils()
m1.add(10) # default value of y is used. 
m1.add(10, 20) # value of both x and y is provided.


# Using variable length argument list.
class MathUtils2:
    def add(self, *args):
        if len(args)==1:
            return args[0]
        elif len(args)==2:
            return args[0]+args[1]
        else:
            return sum(args)

math=MathUtils2()
print(math.add(5))
print(math.add(5,4))
print(math.add(5, 4,3))
print(math.add(5, 4,3, 2,1))


class ShoppingCart:
    def calculate_total(self,*args):
        total=0
        for item in args:
            total+=item
        return total 
    def calculate_total_with_discount(self,discount=0, **kwargs):
        total=0 
        for item,price in kwargs.items():
            total+=price 
        total-=discount
        return total

# Example usage
cart = ShoppingCart()

# Calculate total without discount
total_price = cart.calculate_total(10, 20, 30, 15)
print("Total price without discount:", total_price)  # Output: Total price without discount: 75

# Calculate total with discount
total_price_with_discount = cart.calculate_total_with_discount(discount=10, apple=10, banana=20, orange=30)
print("Total price with discount:", total_price_with_discount)  # Output: Total price with discount: 55


class Shape:
    def calculate_area(self, length, breadth=None):
        if breadth is None:
            return length**2 # area of square.
        else:
            return length*breadth # area of rectangle
    def calculate_area_circle( self,radius):
        return 3.14*radius**2 # area of circle

# Example usage
shape = Shape()

# Calculate area of a square
area_square = shape.calculate_area(5)
print("Area of square:", area_square)  # Output: Area of square: 25

# Calculate area of a rectangle
area_rectangle = shape.calculate_area(4, 6)
print("Area of rectangle:", area_rectangle)  # Output: Area of rectangle: 24

# Calculate area of a circle
area_circle = shape.calculate_area_circle(3)
print("Area of circle:", area_circle)  # Output: Area of circle: 28.274333882308138


area_rectangle =shape.calculate_area(4, 6)
print("Area of rectangle:", area_rectangle)  # Output: Area of rectangle: 24


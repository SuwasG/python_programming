import math

def solve_quadratic(a, b, c):
    # Check if a is zero
    if a == 0:
        return "This is not a quadratic equation (a should not be zero)."
    
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the discriminant is positive, zero, or negative
    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return ("Two distinct real roots", root1, root2)
    elif discriminant == 0:
        # One real root (repeated)
        root = -b / (2*a)
        return ("One real root", root)
    else:
        # Two complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return ("Two complex roots", complex(real_part, imaginary_part), complex(real_part, -imaginary_part))

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Solve the quadratic equation
result = solve_quadratic(a, b, c)

# Display the result
if isinstance(result, str):
    print(result)
else:
    if result[0] == "Two distinct real roots":
        print("The equation has two distinct real roots: {} and {}".format(result[1], result[2]))
    elif result[0] == "One real root":
        print("The equation has one real root: {}".format(result[1]))
    else:
        print("The equation has two complex roots: {} and {}".format(result[1], result[2]))

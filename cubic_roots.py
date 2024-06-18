import math

def cubic_roots(a, b, c, d):
    if a == 0:
        raise ValueError("Coefficient 'a' should not be zero for a cubic equation.")

    # Calculate the discriminant
    f = ((3 * c / a) - ((b**2) / (a**2))) / 3
    g = ((2 * (b**3) / (a**3)) - (9 * b * c / (a**2)) + (27 * d / a)) / 27
    h = (g**2 / 4) + (f**3 / 27)

    if h > 0:
        # One real root and two complex roots
        R = -(g / 2) + math.sqrt(h)
        S = R**(1/3)
        T = -(g / 2) - math.sqrt(h)
        U = T**(1/3)

        real_root = (S + U) - (b / (3 * a))
        return [real_root]
    elif f == 0 and g == 0 and h == 0:
        # All roots are real and equal
        root = -((d / a)**(1/3))
        return [root, root, root]
    elif h <= 0:
        # All roots are real and different
        i = math.sqrt((g**2 / 4) - h)
        j = i**(1/3)
        k = math.acos(-(g / (2 * i)))
        L = j * -1
        M = math.cos(k / 3)
        N = math.sqrt(3) * math.sin(k / 3)
        P = -(b / (3 * a))

        root1 = 2 * j * math.cos(k / 3) - (b / (3 * a))
        root2 = L * (M + N) + P
        root3 = L * (M - N) + P
        return [root1, root2, root3]

def main():
    try:
        a = float(input("Enter the coefficient a: "))
        b = float(input("Enter the coefficient b: "))
        c = float(input("Enter the coefficient c: "))
        d = float(input("Enter the coefficient d: "))
        
        roots = cubic_roots(a, b, c, d)
        print("The roots of the cubic equation are:", roots)
        
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

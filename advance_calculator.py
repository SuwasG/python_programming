import math

def calculate():
    while True:
        print("\nAdvanced Scientific Calculator")
        print("Operations:")
        print("1: Addition (+)")
        print("2: Subtraction (-)")
        print("3: Multiplication (*)")
        print("4: Division (/)")
        print("5: Exponent (**)")
        print("6: Sine (sin)")
        print("7: Cosine (cos)")
        print("8: Tangent (tan)")
        print("9: Square Root (sqrt)")
        print("10: Logarithm (log)")
        print("11: Exit")

        try:
            choice = input("\nEnter the operation number: ")
            if choice.isdigit():
                choice = int(choice)
                if choice == 11:
                    print("Exiting calculator.")
                    break
                if choice in [1, 2, 3, 4, 5, 10]:  # Operations that need two inputs
                    num1 = float(input("Enter the first number: "))
                    if choice != 10:  # Logarithm uses the second number as the base
                        num2 = float(input("Enter the second number: "))

                elif choice in [6, 7, 8, 9]:  # Operations that need only one input
                   num = float(input("Enter the number: "))
                if choice == 10:  # Prompt for base if choice is logarithm
                    base = float(input("Enter the logarithm base: "))
                            # Perform the selected operation
                if choice == 1:
                    print(f"Result: {num1} + {num2} = {num1 + num2}")
                elif choice == 2:
                    print(f"Result: {num1} - {num2} = {num1 - num2}")
                elif choice == 3:
                    print(f"Result: {num1} * {num2} = {num1 * num2}")
                elif choice == 4:
                    if num2 == 0:
                        print("Error: Cannot divide by zero.")
                    else:
                        print(f"Result: {num1} / {num2} = {num1 / num2}")
                elif choice == 5:
                    print(f"Result: {num1} ** {num2} = {num1 ** num2}")
                elif choice == 6:
                    print(f"Result: sin({num}) = {math.sin(math.radians(num))}")
                elif choice == 7:
                    print(f"Result: cos({num}) = {math.cos(math.radians(num))}")
                elif choice == 8:
                    print(f"Result: tan({num}) = {math.tan(math.radians(num))}")
                elif choice == 9:
                    if num < 0:
                        print("Error: Cannot find the square root of a negative number.")
                    else:
                        print(f"Result: sqrt({num}) = {math.sqrt(num)}")
                elif choice == 10:
                    if num1 <= 0 or base <= 1:
                        print("Error: Logarithm undefined for these values.")
                    else:
                        print(f"Result: log base {base} of {num1} = {math.log(num1, base)}")
                else:
                    print("Invalid choice. Please select a valid operation.")
            else:
                print("invalid operator.")

        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")
calculate()

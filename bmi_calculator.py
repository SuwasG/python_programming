def get_float_input(prompt):
    """Prompt the user for a float input, with error checking."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def calculate_bmi(weight, height):
    """Calculate and return the BMI."""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Return the health category based on BMI."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Advanced BMI Calculator")
    # Choose the unit system
    unit_system = input("Choose your unit system (Metric or Imperial): ").strip().lower()

    if unit_system.startswith('m'):
        # Metric units
        weight = get_float_input("Enter your weight in kilograms: ")
        height = get_float_input("Enter your height in meters: ")
    elif unit_system.startswith('i'):
        # Imperial units
        weight = get_float_input("Enter your weight in pounds: ")
        height = get_float_input("Enter your height in inches: ")
        # Convert imperial to metric
        weight = weight * 0.453592
        height = height * 0.0254
    else:
        print("Invalid unit system. Please enter 'Metric' or 'Imperial'.")
        return

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print(f"Your BMI is {bmi:.2f}, which is considered {category}.")


# if __name__ == "__main__": allows you to check if your script is being run directly. This is useful for running code that you don't want to be executed when the file is imported as a module. Therefore, anything inside the if __name__ == "__main__": block will only be executed if the script is run directly, and not when it's imported.
if __name__ == "__main__":
    main()

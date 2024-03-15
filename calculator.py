

def add(num1, num2):
    return num1+ num2

def subtract(num1, num2):
    return num1- num2

def multiply(num1, num2):
    return num1* num2

def divide(num1, num2):
    if num1 == 0 :
        print("zero can not be divided .")
        quit()
    else:
        return num1/num2
    
def exponent(num1, num2):
    return num1** num2


num1= input("Enter a number: ")
num2= input("Enter a number: ")
print('''
    select operators: 
          1. + (addition)
          2. - (subtraction)
          3. * (multiplication)
          4. / (division)
          5. ** (exponent)
        ''')
selectedOperator = input("Enter a operator number: ")

if num1.isdigit() and num2.isdigit() and selectedOperator.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        selectedOperator = int(selectedOperator)
        print("num1: ", num1)
        print("num2: ", num2)
        print( "selectedOperator number: ", selectedOperator)

else: 
        print("invalid numbers and operator. Please enter the valid input.")
    
if selectedOperator ==1:
    print(f"RESULT: {num1} + {num2} = ", add(num1, num2))
elif selectedOperator ==2:
    print(f"RESULT: {num1} - {num2} = ", subtract(num1, num2))
elif selectedOperator ==3:
    print(f"RESULT: {num1} * {num2} = ", multiply(num1, num2))
elif selectedOperator == 4:
    print(f"RESULT: {num1} / {num2} = ", divide(num1, num2))
elif selectedOperator == 5:
    print(f"RESULT: {num1}^{num2} = ", exponent(num1, num2))
else:
     print("Invalid operator and numbers.")

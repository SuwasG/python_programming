'''
Conditional statements decide the control flow(direction) of code (program execution).
Types of control flow in Python:
- if statement
- if-else statement
- nested-if statement
- if-elif-else statemnt.

'''
import datetime

num1 = int(input("Please enter a number: "))

# if statement: most simple decision-making statement.
if num1 > 5:
    print("{} is greater than 5.".format(num1))

print('i am not in if')   
# if-else statement : 
'''
if (condition):
    # Executes this block if
    # condition is true
else:
    # Executes this block if
    # condition is false
'''
num2 = int(input("Please enter a number2: "))
if num2 % 2 == 0:
    print("{} is an even number.".format(num2))  
else:
    print("{} is an odd number.".format(num2))  

# Nested-if statement.
''' 
if (condition1):
   # Executes when condition1 is true
   if (condition2): 
      # Executes when condition2 is true
   # if Block is end here
# if Block is end here
'''
i = 10
if (i == 10):     
    #  First if statement 
    if (i < 15): 
        print("i is smaller than 15") 
          
    # Nested - if statement 
    # Will only be executed if statement above 
    # it is true 
    if (i < 12): 
        print("i is smaller than 12 too") 
    else: 
        print("i is greater than 15") 


# check the leap year
year =int(input("Enter the year"))
if year%4==0  and year%100!=0 or year%400==0:
    print("{} is leap year".format(year))
else:
    print("{} is not leap year".format(year))


# Get the current date
today = datetime.date.today()

# Extract the day of the week as an integer (where Monday is 0 and Sunday is 6)
weekday = today.weekday()

# Use if-elif-else statements to print the corresponding weekday name
if weekday == 0:
    print("Today is Monday.")
elif weekday == 1:
    print("Today is Tuesday.")
elif weekday == 2:
    print("Today is Wednesday.")
elif weekday == 3:
    print("Today is Thursday.")
elif weekday == 4:
    print("Today is Friday.")
elif weekday == 5:
    print("Today is Saturday.")
else:  # weekday == 6
    print("Today is Sunday.")


# match-case
def get_weekday_name(weekday):
    match weekday:
        case 0:
            return "Monday"
        case 1:
            return "Tuesday"
        case 2:
            return "Wednesday"
        case 3:
            return "Thursday"
        case 4:
            return "Friday"
        case 5:
            return "Saturday"
        case 6:
            return "Sunday"
        case _:
            return "Invalid day"

# Getting the current weekday number
current_weekday = datetime.datetime.now().weekday()
print(get_weekday_name(current_weekday))
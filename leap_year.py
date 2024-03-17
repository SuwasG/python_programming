# simple method with conditional statements only.
year = input("Enter the year: ") 
if year.isdigit():
    year = int(year)  
    if year%4==0  and year%100!=0 or year%400==0:
        print(year, "is leap Year")
    else:
        print(year, "is not a leap year.")  
else:
    print("enter the valid year.")
    # quit()


# using the function. to make more user friendly, readable and maintable.
def is_leap_year(year):
    """Check if a given year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_valid_year():
    """Prompt the user for a year until a valid input is given."""
    while True:
        year_input = input("Enter the year: ")
        if year_input.isdigit():
            year = int(year_input)
            return year
        else:
            print("Please enter a valid year. A year should be a number.")

def main():
    year = get_valid_year()
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

main()

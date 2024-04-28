num = input("Enter the number: ")
print(f"Multiplication table of {num} is: ")

try:
    for i in range(1,11):
        print(f"{int(num)} X {i} = {int(num)*i}")
except ValueError:
    print("Number entered is not integer.")
except IndexError:
    print("index error")
except Exception as e:
    print(e)

print("Some lines of code.")
print("End of program.")


# The finally block is executed whether an exception occurs or not. It's commonly used for cleanup operations like closing files or releasing resources
try:
    # Code that may raise an exception
    result = int("hello")  # ValueError: invalid literal for int() with base 10: 'hello'
except ValueError:
    print("ValueError occurred!")
finally:
    # Code that always runs, regardless of whether an exception occurred
    print("Cleanup code")

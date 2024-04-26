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
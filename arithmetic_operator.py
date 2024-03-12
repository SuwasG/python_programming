# operators manipulate the data

# arithmetic operators:
# arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, and divison


'''
+ addition operator
- subtraction operator
* multiplication
/ division
% modulus (gives remainder)
** exponentiation (power)
// floor division (gives the floor of the quotient.)
'''
x = 20
y = 3
sum = x+y
print(sum)
print("The sum is: " + str(sum))
print(f"the sum is {sum}")
print("The sum is {:.2f}".format(sum))

mul = x*y
print(mul)

div = x/y
print(div)

mod = x % y
print(mod)

p=100/3
print("The division is {:.2f}".format(p))


floor = x//y
print(floor)


exp=2**5
print(exp)
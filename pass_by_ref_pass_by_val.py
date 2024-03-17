# In Python, every variable name is a REFERENCE.
# When we pass a variable to the function, a new reference to the object is created.
'''
When you pass a variable to a function in Python, what you're passing is a reference to the object that the variable points to, not the actual object itself. However, how changes to this object behave inside the function depends on whether the object is mutable (like lists, dictionaries, sets) or immutable (like integers, floats, strings, tuples).
'''

# Here n is a new reference to same list
nums=[10,20, 30]
def myFun(n):
    n[0] = 50
    print("nums inside the function: ", nums)
myFun(nums)
print("nums outside the function: ", nums)

# 
def modify_immutable(x):
    x+=10
    print(f"x inside the function: {x}")

a = 5
modify_immutable(a)
print(f"a outside function: {a}")

# mutable object
my_list = [1, 2, 3]
def modify_mutable(lst):
    lst.append(5)  # This modifies the list in place
    print(f"lst inside function: {lst}")

modify_mutable(my_list)
print(f"my_list outside function: {my_list}")

# NOTE: Python's handling of function arguments can be thought of as neither purely pass-by-value nor pass-by-reference. Instead, it's more accurate to say Python uses pass-by-object-reference, where the function receives a reference to the object, not the object itself, but the effect this has depends on the object's mutability.

def swap(x,y):
    temp = x
    x=y
    y=temp
    print(f"values of x and y inside the funcn, x: {x}, y: {y}")
x=2
y=3
swap(x,y)
print(f"values of x and y outside the funcn, x: {x}, y: {y}")
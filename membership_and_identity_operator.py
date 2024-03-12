# membership operator -> Check if any value is a member of that collection or not.
# membership operator tests for membership in a sequence, such as STRINGS, LISTS, TUPLES, SET
# in -> Check that the value is member or not
# not in -> Check that value is not a member or not.

text= "hello world" 
print('h' in text)
print('H' in text)
print('' in text)

print('l' not in text)
print('' not in text)
print('y' not in text)
print('D' not in text)


numbers=[1,2,3,4,5]
print(2 in numbers) # O(n)
print(8 in numbers)
print(8 not in numbers)

print('hello jupyter')


fruits =("Apple", "Banana", "Cherry")
print("Apple in fruits: {}".format('Apple' in fruits))

colors = {"red", "blue", "green", "black", "violet", "indigo", "magenta"}
print("indigo in colors: {}".format("indigo" in colors))  # O(1)


# Identity operator
# Identity operators are used to compare the objects if both the objects are actually of the same datatype and share the same memory location. 
# is -> Evaluates to True if the variables on either side of the operator point to the same, otherwise False.
# is not -> Evaluates to True if both the variables are not the same object.
p = 15
q = 15
r = "15"

print("p is q: {}".format(p is q))
print("p is r: {}".format(p is r))

print("p is not q: {}". format(p is not q))
print("p is not r: {}". format(p is not r))



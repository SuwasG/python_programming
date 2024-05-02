# set: is collection of unique elements in random order.

names ={'Aayush', 'Sujit', 'Suwas', 'Suwas'}
print("names: ", names)
print(type(names))
# Time Complexity: O(1)
# Auxiliary Space: O(1)

# len()
print("len of names: ", len(names))

# adding element to the last: add()
# time complexity: O(n)
# auxiliary space: O(n)
names.add("Smriti")
print("set of names after adding Smriti: ", names)

# heterogenous element with python set
my_set = {"Hello", "Suwas", True, 1, 2, 5,3.69}
print("type of my_set: ", type(my_set))
# Time Complexity: O(n)
# Auxiliary Space: O(n)


# membership operator 'in' and 'not in'
print("Suwas in names: ", "Suwas" in names)
print("Suwas in names: ", "Suwas" not in names)

a = {0,1,2,3,4,5}
b= {4,5,6,7,8,9}
# union
# Time Complexity: O(n)
# Auxiliary Space: O(n)
print("a union b: ", a.union(b))

# intersection
# Time Complexity: O(n)
# Auxiliary Space: O(n)
print("a intersection b: ", a.intersection(b))

# symmetric_difference: gives the unique values on both sets
# Time Complexity: O(n)
# Auxiliary Space: O(n)
print("symmetric_difference btn a and b: ", a.symmetric_difference(b))

# clearing python sets using clear() method:
# Time Complexity: O(n)
# Auxiliary Space: O(n)
set_x= {1,2,3,4}
print('set_x before clearing: ', set_x)
set_x.clear()
print('set_x after clearing: ', set_x)

x = {1, 2, 3, 4, 5, 6}
y = {2, 3, 4}
print(x.issuperset(y)) # issuperset() -> returns whether this set contains another set or not.
print(y.issubset(x)) # issubset() -> returns whether another set contains this set or not.
print(y.isdisjoint(x)) # isdisjoint() -> returns whether two sets have a intersection or not.

subjects = {"python", "java", "javascript", "c", "c++", "c#", "ruby","r","dart"}
print("set of subjects before removing java: ", subjects)

# remove() -> removes the specified item, and if not found then throws KeyError.
subjects.remove('java')
print("set of subjects after removing java: ", subjects)

# discard -> removes the specified item, and if not found then does not throw an error.
# subjects.remove("hello")
# print("set of subjects after removing hello: ", subjects) -> KeyError

subjects.discard('hello')
print("set of subjects after discarding hello: ", subjects)

# pop() -> removes an element from the set.
subjects.pop()
print("set of subjects after popping : ", subjects)

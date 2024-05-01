# list -> it contains collection of more than one data
# python lists are just like dynamically sized arrays, declared in other languages. 
# it is mutable i.e. element inside list can be changed.
# and it is ordered, 
# allow duplicates
# A list is a colllection of thigs, enclosed in [] and separated by commas.

fruits = ['apple', 'banana', 'cherry', 'grapes','apple', 'mango', 'strawberry']
print(fruits)

# Accessing elements from the list: INDEXING

# indexing 
print("items at first position on fruits list: {}".format(fruits[0]))
print("items at last position on fruits list: {}".format(fruits[-1])) # negative indexing: -1 = last item and -2 = second-last item etc.

# Multi-dimensional list
words = [["Hello", "Programming"], ["Namaste", "Python"]]
print("words: ", words)
# accessing elements from a multi-dimensional list.
print("words[1][0]: ", words[1][0])

'''
NOTE: Complexities for Accessing elements in a List:
TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
'''

# len() -> to get the size of python list
print("size of fruits list: ", len(fruits))
print("size of words list: ", len(words))

# count() -> counts the elements
print("apple count in fruits: ", fruits.count("apple"))

# list slicing
print("fruits[0:3]", fruits[0:3])
print("fruits[0:3]", fruits[3:])
print("fruits[0:3]", fruits[-4:-2])
print("fruits[0:3]", fruits[-4:])

# index() -> returns the lowest index where the element appears
print("index of apple is: ", fruits.index("apple"))


# updating the list elements
print("fruits without updated value at index 2: ", fruits)
fruits[2]="papaya"
print("fruits with updated value at index 2: ", fruits)

fruits[-2]= 'guava'
print("fruits after updating value at second last position: ", fruits)


# append(value) -> add the single element at a time in the last position
#  Time Complexity: O(1) , Space complexity: O(1)
fruits.append("kiwi")
print("fruits after appending kiwi: ", fruits)

# insert(position, value) -> add the elements at the desired positions.
# Time complexity : O(n), Space Complexity: O(1)
fruits.insert(3,"pear")
print("fruits after inserting pear at index 3: ", fruits)

# extend(value) ->adds at the last position used to add multiple elements at a time.
#  Time complexity : O(n), Space complexity : O(1)
fruits.extend(["blueberry", "mulberry", "blackberry"])
print("fruits after extending berries: ", fruits)

# remove() -> remove elements from the list but an ERROR arises if the element doesn't exist in the list.
# Time complexity: O(n)
# Space complexity: O(1)
fruits.remove("banana")
print("fruits after removing banana: ", fruits)

# fruits.remove("plum")
# print("fruits after removing the plum which is not the element of list: ", fruits) #-> thows ValueError.

nums = [1,2,3,4,5,6,7,8,9,10]
# to remove the range of elements, the iterator is used.
for n in range (1,5):
    nums.remove(n)
print("nums after removing a range of elements: ", nums)

# pop() -> by default, it removes only the last element of the list, to remove an element from specific position of the list, the index of the element is passed as an argument to the pop() method.

colors = ['red', 'blue', 'green', 'violet', 'purple', 'black']
print("colors: ", colors)
print("remvoing the last color of colors using pop: ", colors.pop())
print("colors: ", colors)
print("remvoing the second(index=1) color of colors using pop: ", colors.pop(1))
print("colors: ", colors)


# clear()-> removes all items/elements from the list.
veg = ['cauliflower', 'cabbage','lettuce']
print("veg: ", veg)
print("veg after clear: ", veg.clear())
print(type(veg))

# REVERSING a List
# method 1: using reverse()-> 
my_list = [2,3,5,7,11,13,17,19,23,29, "even", 'odd']
print("my_list: ", my_list)
my_list.reverse()
print("my_list after reversing: ", my_list)

# method 2: using reversed()->
my_list2 = [2,3,5,7,11,13,17,19,23,29]
reversed_my_list2 = list(reversed(my_list2))
print("reversed_my_list: ", reversed_my_list2)

# sorting
numbers = [1, 2, 5, 9, 8, 1, 3, 2, 7, 9, 11, 3, 29, 5, 3, 5]
print("numbers before sorting: ", numbers)

numbers.sort()
print("numbers after sorting: ", numbers)

# min()-> calculates the minimum of all the elements in the list
print("min(): ", min(numbers))

# min()-> calculates the minimum of all the elements in the list
print("max(): ", max(numbers))

# Taking Input of a Python List:
userInput = input("Enter elements (space-separated): ")

# split the string(userInput) and store it to a list.
list_input = userInput.split()
print("The list of input is: ", list_input)

userInput2 = input("Enter elements (comma-separated): ")

# split the string(userInput) and store it to a list.
list_input2 = userInput2.split(',')
list_input2 = [element.strip() for element in list_input2] # to remove white spaces
print("The list of input2 is: ", list_input2)
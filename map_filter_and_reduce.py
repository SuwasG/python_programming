# Map Function: The map() function applies a specified function to all items in an iterable (such as a list) and returns a new iterable with the results.

# Example 1: Doubling the numbers in a list using map
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)
print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10]

# Example 2: Converting list of strings to uppercase
names = ["alice", "bob", "charlie"]
uppercase_names = map(str.upper, names)
print(list(uppercase_names))  # Output: ['ALICE', 'BOB', 'CHARLIE']


# Filter Function: The filter() function filters elements from an iterable based on a specified condition, and returns an iterator containing the elements that satisfy the condition.
# Example: Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]


# Reduce Function: The reduce() function, which was previously a built-in function in Python 2.x but is now available in the functools module, applies a rolling computation to sequential pairs of values in an iterable, reducing them to a single value.

# Example: Summing all numbers in a list using reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15

str1 = 'Single Quoted String.' # string with single quotes
str2 = "Double Quoted String." # string with double quotes
str3 = '''Triple 
    Quoted 
    String''' # string with triple quotes

print("str1: ", str1)
print("str2: ", str2)
print("str3: ", str3)



text = 'Python is a high level programming language. It is mainly used in the field of Artificial Intelligence.'

# text indexing
print(text[5])

# negative indexing
print(text[-5])

print("First character of String:" , text[0])
print("Last character of String: ", text[-1])


# text slicing
# In Python, the String Slicing method is used to access a range of characters in the String
print(text[0:20])

# negative slicing
print(text[-20:-1])

print(text[:25])

print(text[20:])

print(text[:])

# reversing a python string
# method 1 -> using the slicing
str = "hellosuwas"
print("reversing a python string: " ,str[::-1])

# method 2 -> using python built in join and reversed functions.
str = "".join(reversed(str))
print("reversing python string using built in functions: ", str)
# count the number of characters in string:
print(len(text))

# upper() -> uppercase letter 
print(text.upper())

# lower() -> lowercase letter 
print(text.lower())

# split()
print(text.split("."))
print(text.split("a"))

# count
print(text.count('a'))

# replace() -> returns a copy of the string where occurrences of a substring are replaced
# with another substring.
string8 = "Hello Python Programming"
new_string8= string8.replace("Programming", "Coding")
print("replace Programming with Coding: ", new_string8)

# deleting a character of string
string1 = "Hello, Programming."
print("string1 before character deletion: ", string1)

# del string1[2] -> this gives the TypeError: 'str' object doesn't support item deletion
# print("string1 after deleting the character on index 2: ", string1)


# deleting entire string
del string1
# print(string1) # NameError: name 'string1' is not defined because the string1 is already deleted and is unavailable to be printed.


# escape sequencing:
# escape characters start with a backslash and can be interpreted differently.
string2= '''I'm a "Suwas" '''
print(string2)

# escaping single quote
string2 = 'I\'m a "Suwas"'
print(string2)

# escaping double quote
string2 = "I'm a \"Suwas\""
print(string2)

# To ignore escape sequences in a string, r or R is used, this implies that the string is a raw string and escape sequences inside are to be ignored.
string3 = "This is \110\145\154\154\157"
string4 = r"This is \110\145\154\154\157"
print("string3 without r or R i.e. printing in Octal: ", string3)
print("string4 with r or R i.e. printing the raw string.: ", string4)


# Formatting of String
# Strings in Python can be formatted with the use of format() method.
# format() method in Strings contains curly braces {} as placeholders which can hold arguments according to the position or keyword to specify the order.

# Default order
string5 = "{} {} {} {}".format("Hello", "From","Suwas", "Ghale")
print("string5 with default order format: ", string5)

# Positional formatting
string6 = "{3} {2} {0} {1}".format("Hello", "From","Suwas", "Ghale")
print("string6 with positional format: ", string6)

# keyword formatting
string7 = "{s} {g} {f} {h}".format(h="Hello", f="From",s="Suwas", g="Ghale")
print("string7 with keyword format: ", string7)

# Formatting of Integers
str5 = "{0:b}".format(16)
str6 = "{0:b}".format(11)
print("Binary representation of 16 is: ", str5)
print("Binary representation of 11 is: ", str6)

# Formatting of Floats
str7 = "{0:e}".format(123.6458)
str8 = "{0:e}".format(1234.4458)
print("Exponent representation of 123.6458 is: ", str7)
print("Exponent representation of 1234.4458 is: ", str8)


# Rounding off integers:
str9 = "{0:.5f}".format(22/7)
str10 = "{0:.3f}".format(1/7)
print("22/7 is: ", str9)
print("1/7 is: ", str10)


# String alignment
'''
->A string can be left, right or center aligned with the use of format specifiers,   separated by a colon(:). 
-> The (<) indicates that the string should be aligned to the left.
-> The (>) indicates that the string should be aligned to the right.
-> The (^) indicates that the string should be aligned to the center.

for eg: (<10) means that the string should be aligned to the left within a field of width
of 10 characters.

'''
str11 = "|{:<10}|{:^10}|{:>10}".format("Suwas", "Is", "Ambitious")
print("string alignment str11: ", str11)


# looping 
for char in text:
    print(char)


# Assignment for later:
# 1. Find all duplicate characters in string.
# 2. Reverse string in Python (5 diff methods.)
# 3. Write a python program to check whether the string is palindrome or not.
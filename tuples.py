# tuple: is a collection of objects separated by commas.
# tuple can be indexed, ordered and allow duplicates.
# tuple are IMMUTABLE while list are MUTABLE.


# creating tuples in Python
# using parenthesis
fruits = ('apple', 'banana', 'cherry', 'apple', 'mango', 'orange', 'papaya')
print("fruits: ", fruits)
print("type of fruits: ", type(fruits))

# tuple constructor:
languages = ('python', 'javascript', 'java', 'ruby')
print("type of languages: ", type(languages))
tuple_constructor = tuple(languages)
print(type(tuple_constructor))

# indexing
print("fruits[2]: ", fruits[2])
print("fruits[4]: ", fruits[4])

# negative indexing
print("fruits[-1]: ", fruits[-1])
print("fruits[-3]: ", fruits[-3])

# slicing
print("fruits[0:3]", fruits[0:3])
print("fruits[-4:-2]", fruits[-4:-2])

# count()
print("apple in fruits: ", fruits.count("apple"))

# index()
print("index of apple in fruits: ", fruits.index("apple"))
print("index of mango in fruits: ", fruits.index("mango"))

# loop
for f in fruits:
    print(f)

# concatenation of python tuples
tuple1= (0, 1, 2,3,4, 5)
tuple2= ("Hello", "Suwas")
print("concatenating tuples: ", tuple1+tuple2)

# Nesting of python tuples
tuple3 = (tuple1, tuple1)
print("nested tuple3: ", tuple3)

# repetition python tuples
print("repetition tuple2 for 3 times: ", tuple2*3)

# len()
print( "len of tuple2: ",len(tuple2))

# tupple with different data types:
tuple5 = ("suwas", 1,2, True, 3.14)
print("tuple5: ", tuple5)
print("type of tuple5: ", type(tuple5))

# converting list to tuple
my_list =[1,3, 5, 7, 9]
print("type of my_list: ", type(my_list))
print("my_list to tuple: ", tuple(my_list))
print("type of my_list: ", type(tuple(my_list)))

# dictionary is the data type use to store data in key value pairs.

student ={
    'first_name':"Suwas",
    "last_name":"Ghale",
    'age':22,
    "gender":"Male", 
    "address":"Rasuwa", 
    "isMarried":False,
    'subjects':['python', 'javascript', 'java', 'c']
}
print(type(student))
print(student)

# dictionary length: len()
print("len of student dictionary: ", len(student))

# using dict() consturctor to make a dictionary
my_dictionary = dict(name="Suwas", age=22, country='Nepal', eduction='Bachelor')
print(my_dictionary)

# Accessing dictionary items
print("age of student: ", student['age'])
# print("hello of student: ", student['hello']) -> gives KeyError

print("hello of student: ", student.get('hello'))
print("subjects of student: ", student.get('subjects')) 

# get the list of keys()
print("list of keys for dictionary student: ", student.keys())
student['height'] = 165
print("len of student dictionary after adding key height: ", len(student))
print("list of keys for dictionary student: ", student.keys())

# get the list of values()
student['height'] = 170
print("list of values for dictionary student: ", student.values())

# get the list of key:value pairs -> items()
print("list of key:value pairs for dictionary student: ", student.items())


# update -> updates the dictionary with specified key-value pairs.
student.update({"address":"Kathmandu"})
print("sutdent: ",student)

# access the inner lists
print(student.get('subjects')[1])

# updating the inner list values
student['subjects'][1]='TypeScript'
print("sutdent: ",student)

# pop -> removes the element with the specified key.
print("pop: ",student.pop("height"))
print("sutdent: ",student)

# popitem -> removes the last inserted key-value pair
print("popitem: ",student.popitem())
print("sutdent: ",student)

# nested dictionary:
dict1={
    "key1":"value1",
    "dict2":{
        "key2a":"value2a",
        "key2b":"value2b",
        "key2c":"value2c",
    },
    "key3":"value3",
    "key4":"value4"
}
print(dict1)
d= dict1['dict2']
print("d: ",d)
print("len of inner dictionary d: ", len(d))

print( "keys of dict2: ", d.keys())
print( "values of dict2: ", d.values())
print( "items of dict2: ", d.items())

d.pop("key2b")
print("d after popping key2b: ",d)

d.popitem()
print("d after popping items: ",d)

d['key2d'] ='value2d'
print('d after adding key2d: ', d)


for x,y in dict1.items():
    print(x,"->" ,y)

for p, q in d.items():
    print(p , "->", q)


# in => used to check if a specified key is present in a dictionary.
if "age" in student:
    print("Yes age is one of the key in student dictionary.")
else:
    print("age key is not found in student dictionary.")

demo_dictionary={
    "greetings":"Hello",
    "welcome":"Bienvenue",
    "isOkay":True,
}
print("demo_dictionary: ", demo_dictionary)
# clear() -> empties the dictionary
demo_dictionary.clear()
print("clear demo_dictionary: ", demo_dictionary)
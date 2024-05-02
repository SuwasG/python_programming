# loop: A loop is an instruction that repeats multiple times as long as some condition is met.

# loops -> repeatation or iteration.
# mainly there are two types of loops in python: 1. for loop and 2. while loop

# 1. for loop
# for loop is used to iterate over a sequence (list,tuple, set, dictionary and string.)

# iterate through a list
subjects = ['python', 'javascript', 'java', 'c', 'c++', 'c#']

for subs in subjects:
    print(subs)
# in the above for loop code, the variable subs is a placeholder for every item in our iterable object(list).
# The loop iterates as many times as the number of elements and prints the elements serially.

# iterate through string.
text = "Statements"
for char in text:
    print(char)

# iterate through tuples
colors = ("red", "blue", "black", 'green', 'yellow')
for cols in colors:
    print(cols)

# iterate through dictionary
student ={
    "name":"Suwas",
    "address":"Rasuwa",
    "age":22,
    "isMarried":False,
    "courses":['full-stack web dev', 'flutter dev', 'data science', 'database', 'networking']
}
for keys in student.keys():
    print(keys)
for vals in student.values():
    print(vals)
for keys,vals in student.items():
    print(keys , '-> ', vals)

# iterate through set
fruits ={'apple', 'banana', 'cherry', 'mango', 'papaya', 'avocado', 'apple'}
print("type of fruits: ", type(fruits))

for f in fruits:
    print(f)

# iterating by the index of sequences
print('-------iterating by the index of sequences------')
subjects = ['python', 'javascript', 'java', 'c', 'c++', 'c#']
for index in range(len(subjects)):
    print(subjects[index])

# range
for n in range(10):
    print(n)

for m in range(1,10):
    print("Hello ", m)

for p in range(1,20,2):
    print("Suwas ", p)
else:
    print("Executed once after completing the for loop.")



# while loop
# The while loop is used to execute a set of statements as long as a condition is true.
print("------while loop ---------")
y = 1
while y<5:
    print("while ", y)
    y+=1
# We assign the value to variable y as 1. 
# Until the value of y is less than 5, the loop continues and prints the while with numbers.

q=20
while q>=1:
    print(q)
    q-=1

# while loop with else statement.
count = 0
while count<5:
    print("Hello Suwas", count)
    count+=1
else:
    print("In the else block of while loop.")


# Nested loop
# loop inside the body of another loop is called nested loop.
print('-----------nested loop-------------')
subs = ['python', 'javascript', 'java', 'c', 'c#']
nums = [1,2,3]

for s in subs:
    for n in nums:
        print(s, n)


for i in range(1,6):
    for j in range(i):
        print(i, end=' ')
    print()

n = 10
sum =0

while True:
    sum+=n
    n-=1
    if n==0:
        break
print("sum of first 10 numbers is: ", sum)


while True:
    userInput = input("Enter a number for which to create a table: ")
    if userInput.isnumeric():
        num = int(userInput)
        for i in range(1, 11):
            print(f"{num} X {i} = {num*i}")
        break  # To exit after printing the multiplication table
    else:
        print("Please enter a valid number.")

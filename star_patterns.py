'''
NOTE: Steps to solve the star patterns: 
i. Understand the patterns.
ii. Initialize the loop for the rows. n=5
iii. Nested loop for printing stars and spaces.

'''

# square star pattern
print("---------squared star pattern--------")
n=5 
for i in range(n):
    for j in range(n):
        print("*", end='')
    print()

# triangle
print('------triangle------')
for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            print("*", end='')
        else:
            print(" ", end='')
    print()

print("---------triangle-2-------------")
n=6
for i in range(1,n):
    for j in range(1,n):
        if j>=n-i:
          print("*", end='')
        else:
            print(" ", end='')
    print()

print("---inverted triangle-----")
for i in  range(1,n):
    for j in range(1,n):
        if j<=n-i:
            print("*", end='')
        else:
            print(" ", end='')
    print()

print("---inverted triangle-2-----")
for i in  range(1,n):
    for j in range(1,n):
        if j>=i:
            print("*", end='')
        else:
            print(" ", end='')
    print()
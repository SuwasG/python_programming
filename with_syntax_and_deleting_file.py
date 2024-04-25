with open('demo.txt', 'r') as f:
    data=f.read()
    print(data)


with open('demo2.txt', 'w') as f:
    f.write("This is demo file. \nCreated by Suwas Ghale")


# deleting a file
'''
Using the os module
Module (Like a code library) is a file written by another programmer that generally has a functions we can use.
'''

import os 
filename='demo2.txt'
if os.path.exists(filename):
    os.remove(filename)
else:
    print("No files found.")
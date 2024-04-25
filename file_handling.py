f=open('demo.txt', 'r')
# data=f.read() # reads entire line
# print(data)
# print(type(data))

line1=f.readline() # reads one line at a time.
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)
line4=f.readline()
print(line4)
line5=f.readline()
print(line5)
line6=f.readline()
print(line6)
line7=f.readline()
print(line7)


f.close()


# write-> overwrites
f2=open('write.txt', 'w')
f2.write("Hi This is write")
f2.close()


# append-> adds 
f3=open('write.txt', 'a')
f3.write("\nThis is appended on write.txt file.")
f3.close()

# r+ -> reading and writing, does not truncate the original file
f4=open('demo.txt', 'r+')
f4.write("Hello")
print(f4.read())
f4.close()


# w+ -> reading + writing with truncate
f5=open("hello.txt", 'w+')
print(f5.read())
f5.write("Hi Namste From Suwas Ghale.")
print(f5.read())
f5.close()

# a+ -> reading + writing and append on last
f6=open("hello.txt", 'a+')
print(f6.read())
f6.write("This is appended +.")
print(f6.read())
f6.close()
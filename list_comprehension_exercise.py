'''
Write a Python Program to read 10 elements in a list from users and then use list comprehension to find and display odd and even numbers in the list.
'''

num_list=[]

for n in range(10):
    user_input=int(input("Enter the number: "))
    num_list.append(user_input)

print(num_list)

odd_nums=[nums for nums in num_list if nums%2!=0]
even_nums=[nums for nums in num_list if nums%2==0]

print("Odd nums: ", odd_nums)
print("Even nums: ", even_nums)
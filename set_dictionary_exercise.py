'''
You are given a list of student names and their corresponding marks in a class. Using dictionaries and sets, write a Python Program to perform the following tasks. 
a) Create a dictionary where the keys are student names and the values are their marks. 
b) Calculate and display the average marks of all students. 
c) Identify and display the students with the highest mark. 
d) Create a set of students who scored below the average mark.
e) Provide options for sorting the student data, such as sorting by name and also by marks in ascending or descending order.
f) Calculate and display additional statistics, such as the median, mode, and standard deviation of the marks.

'''

student_names=[]
student_marks=[]
for s in range(2):
    name=input("Enter the name of student: ")
    student_names.append(name)
    mark=int(input("Enter the mark of student: "))
    student_marks.append(mark)

# a) create a dictionary where keys are student names and values are their corresponding mark.
student_data=dict(zip(student_names, student_marks))
print(student_data)

# b) calculate and display the average marks of all students
total_marks=sum(student_data.values())
average_mark=total_marks/len(student_data)
print("Average mark is: ", average_mark)

# c) Identify and display the students with highest mark.
highest_mark=max(student_data.values())
top_students=[name for name, mark in student_data.items() if mark==highest_mark]
print("Top students: ", top_students)


# d) set of students who scored below the average mark
below_average={name for name, mark in student_data.items() if mark<average_mark}
print("Students with below average marks: ", below_average)


# e) sorting by name and  also by mark
sorting_by_names=sorted(list(student_data.keys()))
print('Sorted names: ', sorting_by_names)

sorting_by_marks=sorted(list(student_data.values()))
print('Sorted marks: ', sorting_by_marks)


# f) Calculate and display additional statistics, such as the median, mode, and standard deviation of the marks.
# calculate the median
def calculate_median(marks):
    sorted_marks=sorted(student_data.values())
    n=len(sorted_marks)
    if n%2==0:
        return (sorted_marks[n//2 -1 ] + sorted_marks[n//2])/2
        # 1 2 3 4 5 6 -> (sorted_marks[6//2 -1] + sorted_marks[6//2])/2
        # -> (sorted_marks[2] + sorted_marks[3])/2
        # (3+4)/2= 3.5
    else:
       return sorted_marks[n//2]

# calculate the mode
def calculate_mode(marks):
    frequency={}
    for m in marks:
        frequency[m] = frequency.get(m, 0) + 1
    max_frequency=max(frequency.values())
    mode=[m for m, frequency in frequency.items() if frequency==max_frequency]
    return mode 

# custom function to calculate the standard deviation
def calculate_standard_deviation(marks):
    mean=sum(marks)/len(marks)
    squared_diff_sum=sum((mark-mean)**2  for mark in marks)
    return (squared_diff_sum/len(marks))**0.5



# Calculate median
median = calculate_median(student_data.values())
print("Median:", median)

# Calculate mode
mode = calculate_mode(student_data.values())
print("Mode:", mode)

# Calculate standard deviation
standard_deviation = calculate_standard_deviation(student_data.values())
print("Standard Deviation:", standard_deviation)



# student_data = {}

# while True:
#     name = input("Enter the name of student (or 'done' to finish): ")
#     if name.lower() == 'done':
#         break
#     mark = int(input("Enter the mark of student: "))
#     student_data[name] = mark

# # b) calculate and display the average marks of all students
# total_marks = sum(student_data.values())
# average_mark = total_marks / len(student_data)
# print("Average mark is: ", average_mark)

# # c) Identify and display the students with highest mark.
# highest_mark = max(student_data.values())
# top_students = [name for name, mark in student_data.items() if mark == highest_mark]
# print("Top students: ", top_students)

# # d) set of students who scored below the average mark
# below_average = {name for name, mark in student_data.items() if mark < average_mark}
# print("Students with below average marks: ", below_average)

# # e) sorting by name and also by mark
# sorting_by_names = sorted(student_data.keys())
# print('Sorted names: ', sorting_by_names)

# sorting_by_marks = sorted(student_data.items(), key=lambda x: x[1])
# print('Sorted marks: ', sorting_by_marks)

# # f) Calculate and display additional statistics
# # Calculate median
# sorted_marks = sorted(student_data.values())
# median = calculate_median(sorted_marks)
# print("Median:", median)

# # Calculate mode
# mode = calculate_mode(sorted_marks)
# print("Mode:", mode)

# # Calculate standard deviation
# standard_deviation = calculate_standard_deviation(sorted_marks)
# print("Standard Deviation:", standard_deviation)

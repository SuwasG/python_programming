'''
Write a Python program to demonstate how a function can be used to send, recieve and return multiple values.
'''

# NOTE: In Python, a function can return multiple values by using tuples, lists, dictionaries and other iterable types.
# using tuple
print("----------using tuple------------")
def send_receive_return_tuple(send_value1,send_value2):
    # send_value1="Hello"
    # send_value2="Suwas"
    return send_value1, send_value2

# calling function and receiving multiple values: 
recieved_value1, recieved_value2=send_receive_return_tuple("Suwas", "Ghale")

# Printing the values
print(f"Recieved value1:{recieved_value1} ")
print(f"Recieved value2:{recieved_value2} ")


# using list
print("----------using list------------")
def send_receive_return_list(send_values=[]):
    # send_values=["Hello", "Sansar"]
    return send_values

# calling function and receiving multiple values: 
recieved_value1, recieved_value2=send_receive_return_list(["Okay", "List"])

# Printing the values
print(f"Recieved value1:{recieved_value1} ")
print(f"Recieved value2:{recieved_value2} ")

# using dictionary
print("----------using dictionary------------")
def send_receive_return_list():
    send_values={"name":"Suwas","age":22}
    return send_values.values()

# calling function and receiving multiple values: 
recieved_value1, recieved_value2=send_receive_return_list()

# Printing the values
print(f"Recieved value1:{recieved_value1} ")
print(f"Recieved value2:{recieved_value2} ")


# using set
print("----------using set------------")
def send_receive_return_list():
    send_values={"Sagar", "Suwas", True, 50, "Suwas"}
    return send_values

# calling function and receiving multiple values: 
recieved_value1, recieved_value2, recieved_value3, recieved_value4=send_receive_return_list()

# Printing the values
print(f"Recieved value1:{recieved_value1} ")
print(f"Recieved value2:{recieved_value2} ")
print(f"Recieved value2:{recieved_value3} ")
print(f"Recieved value2:{recieved_value4} ")

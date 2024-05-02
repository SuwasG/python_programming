# nested functions: Also known as Inner Function.
# A function defined inside another function is known as nested function. (function within function)
# Nested functions are used so that they can be protected from everything happening outside the function.

def outerFun():
    text = "Hello Suwas Ghale."

    def innerFun():
        print(text)
    innerFun()

outerFun()


def createEventGreeting(event_name):
    # Base greeting message for the event
    base_greeting = f"Welcome to {event_name}!"

    # Nested function to personalize the greeting for each attendee
    def greetAttendee(attendee_name):
        # Personalizing the base greeting with the attendee's name
        personalized_greeting = f"{base_greeting} Hello, {attendee_name}."
        print(personalized_greeting)

    # Return the nested function so it can be used outside
    return greetAttendee

# Creating a greeting function for a specific event
eventGreeting = createEventGreeting("Tech Conference 2024")
# Greeting attendees by name
eventGreeting("Suwas Ghale")
eventGreeting("Alex Johnson")


# Anonymous function: A function without a name.
# lambda keyword is used to create anonymous function in Python.
def cube(n):
    return n**3
print(cube(5))

cube_n = lambda x:x**3
print(cube_n(5))


# Recursive Function in Python
# Recursion in Python refers to when a function calls itself.
# Recursive functions in Python are functions that call themselves in order to break down a problem into smaller, more manageable parts.
# A recursive function must have a base condition that stops the recursion, otherwise, it will run indefinitely, leading to a stack overflow error
# When creating a recursive function, it is crucial to carefully check your exit statement to prevent it from becoming a non-terminating loop, akin to exercising caution similar to when using recursive functions.


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print(factorial(6))

# fibonacci sequence with memoization
def fibonacci(num, memo={}):
    """
    Calculate the nth Fibonacci number using memoization to optimize recursive calls.
    fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
    Args:
    - n (int): The position in the Fibonacci sequence.
    - memo (dict): A dictionary to store previously computed Fibonacci numbers.
    
    Returns:
    - int: The nth Fibonacci number.
    """
    if num in memo: # checks if the result is in memo.
        return memo[num]
    elif num<=1: # base case
        return num
    else: # recursive step with memoization
        memo[num]= fibonacci(num-1, memo) + fibonacci(num-2, memo)
        return memo[num]
print(fibonacci(10))



def generate_fibonacci(limit):
    fib_sequence = [0, 1]
    while True:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        if next_num > limit:
            break
        fib_sequence.append(next_num)
    return fib_sequence

limit = int(input("Enter the limit for Fibonacci numbers: "))
fibonacci_numbers = generate_fibonacci(limit)
print("Fibonacci numbers up to", limit, "are:", fibonacci_numbers)


# Tower Of Hanoi using recursive function
'''
Rules: 
1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3. No disk may be placed on top of a smaller disk.
'''

def tower_of_hanoi_with_count(n, source, destination, helper):
    """
    Solves the Tower of Hanoi puzzle.
    Args:
    - n (int): The number of disks.
    - source (str): The initial rod.
    - destination (str): The rod to which disks need to be moved.
    - helper (str): The auxiliary or helper rod.

    Returns:
    - int: The total number of moves required.
    """
     
    if n==1:
        print(f"Move disk 1 from rod {source} to rod {destination}.")
        return 1 # Return the count of moves, which is 1 for the base case
    else:
         # Recursively move n-1 disks from source to helper, print the steps, and count the moves
        moves = tower_of_hanoi_with_count(n-1, source, helper, destination)
        # Print the move of the nth disk from source to destination
        print(f"Move disk {n} from rod {source} to rod {destination}.")
        # Increment the move count by 1 for the current move
        moves += 1
        # Recursively move n-1 disks from helper to destination, print the steps, and update the move count
        moves += tower_of_hanoi_with_count(n-1, helper, destination, source)
        return moves  # Return the total count of moves
 

n=5
total_moves = tower_of_hanoi_with_count(n, 'A', 'B', 'C')
print(f"Total number of moves required: {total_moves}")
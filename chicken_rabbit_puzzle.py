
'''
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

'''

def solve_puzzle(heads, legs):
    for chickens in range(heads+1):
        rabbits=heads-chickens
        if (2*chickens + 4*rabbits)== legs:
            return chickens, rabbits
    return "No Solution."


# Given data
total_heads = 35
total_legs = 94

# Solve the puzzle
solution = solve_puzzle(total_heads, total_legs)

# Print the solution
if solution != "No solution":
    chickens, rabbits = solution
    print("Number of chickens:", chickens)
    print("Number of rabbits:", rabbits)
else:
    print("No solution found.")
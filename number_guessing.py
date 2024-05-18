import random

def get_int_input(prompt, low=None, high=None):
    """Prompt the user for an integer input within optional bounds."""
    while True:
        try:
            value = int(input(prompt))
            if (low is not None and value < low) or (high is not None and value > high):
                print(f"Please enter a number between {low} and {high}.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")

def choose_difficulty():
    """Let the user choose the difficulty level and set the range accordingly."""
    print("Choose difficulty level:")
    print("1: Easy (1-10)")
    print("2: Medium (1-100)")
    print("3: Hard (1-1000)")
    level = get_int_input("Enter difficulty (1-3): ", 1, 3)
    
    if level == 1:
        return 1, 10
    elif level == 2:
        return 1, 100
    elif level == 3:
        return 1, 1000

def number_guessing_game():
    """Play a number guessing game with the user."""
    print("Welcome to the Number Guessing Game!")
    low, high = choose_difficulty()
    number_to_guess = random.randint(low, high)
    
    print(f"Guess a number between {low} and {high}.")

    attempts = 0
    while True:
        guess = get_int_input("Enter your guess: ", low, high)
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low, try again.")
        elif guess > number_to_guess:
            print("Too high, try again.")
        else:
            print(f"Congratulations! You've guessed the right number in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()




import random

def play_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while not guessed_correctly:
        try:
            # Ask the user for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Provide feedback on the guess
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                guessed_correctly = True
        except ValueError:
            # Handle invalid input
            print("Invalid input! Please enter a valid number.")

def main():
    while True:
        play_game()

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()

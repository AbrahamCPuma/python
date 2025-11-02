# Import the 'random' module to generate the secret number.
import random

# --- Constants (Global Scope) ---
# It's a good convention to put constants in all caps.
# These define the number of turns for each difficulty level.
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def check_answer(guess, answer, turns):
    """Checks the user's guess against the answer and returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        # We don't subtract a turn because the game is won.
        return turns

def set_difficulty():
    """Asks the user for a difficulty and returns the number of attempts."""
    # Get user input and return the corresponding number of attempts.
    level = input("Choose a difficulty. Type 'easy' or 'hard':\t").lower()
    if level == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def game():
    """Main function to run the number guessing game."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate the secret number for this game session.
    answer = random.randint(1, 100)
    
    # Set the number of attempts based on the chosen difficulty.
    attempts = set_difficulty()
    
    guess = 0 # Initialize guess to a value that can't be the answer.
    
    # The main game loop continues as long as the guess is not correct.
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:\t"))
        
        # Check the guess and update the number of remaining attempts.
        attempts = check_answer(guess, answer, attempts)
        
        # Check for game over conditions.
        if attempts == 0 and guess != answer:
            print("You've run out of guesses, you lose.")
            print(f"The number was {answer}")
            return # Exit the function
        elif guess != answer:
            print("Guess again.")

# This makes the script runnable by calling the main game function.
game()

        
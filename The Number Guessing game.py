import random

# --- Constants (Global Scope) ---
# It's a good convention to put constants in all caps.
# These are accessible everywhere in the script.
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
    level = input("Choose a difficulty. Type 'easy' or 'hard':\t").lower()
    if level == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def game():
    """Main function to run the number guessing game."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # This variable 'answer' is local to the game() function.
    answer = random.randint(1, 100)
    
    # 'attempts' is also local to the game() function.
    attempts = set_difficulty()
    
    guess = 0 # Initialize guess to a value that can't be the answer.
    
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:\t"))
        
        attempts = check_answer(guess, answer, attempts)
        
        if attempts == 0 and guess != answer:
            print("You've run out of guesses, you lose.")
            print(f"The number was {answer}")
            return # Exit the function
        elif guess != answer:
            print("Guess again.")

# This makes the script runnable.
game()

        
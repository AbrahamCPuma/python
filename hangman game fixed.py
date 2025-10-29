import random
import os
import json
gamewords = ["owl","bunny","elephant","fox","camel","orangutan","zebra","antelope","baboon","cheetah","dolphin","elephant","flamingo","gorilla","hyena","iguana","jaguar","koala","lemur","meerkat","narwhal","ocelot","panda","quetzal","rhino","salamander","toucan"]
randomword = random.choice(gamewords)
numletters = len(randomword)
blankletters = "_ " * numletters
hanglist = []
attempts = 0
guesslist = []
game_over = False

LEADERBOARD_FILE = 'leaderboard.json'

def clear_screen():
    """Clears the output screen. Works in standard terminals and Google Colab."""
    try:
        # This works in Google Colab
        from google.colab import output
        output.clear()
    except ImportError:
        # This works in standard terminals (Windows, macOS, Linux)
        os.system('cls' if os.name == 'nt' else 'clear')

def load_leaderboard():
    """Loads the leaderboard from a JSON file."""
    try:
        with open(LEADERBOARD_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is empty/corrupt, return an empty list
        return []

def save_leaderboard(word, attempts, result):
    """Saves a new score to the leaderboard."""
    leaderboard = load_leaderboard()
    leaderboard.append({'word': word, 'attempts': attempts, 'result': result})
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(leaderboard, f, indent=4)

def display_leaderboard():
    """Displays the top 10 winning scores."""
    leaderboard = load_leaderboard()
    wins = [score for score in leaderboard if score['result'] == 'win']

    # Sort wins by the number of attempts (fewer is better)
    sorted_wins = sorted(wins, key=lambda x: x['attempts'])

    print("\n--- LEADERBOARD (Top 10 Wins) ---")
    if not sorted_wins:
        print("No wins recorded yet. Be the first!")
    else:
        for i, score in enumerate(sorted_wins[:10]):
            print(f"{i+1}. Guessed '{score['word']}' with {score['attempts']} wrong attempts.")
    print("---------------------------------")

# --- ASCII Art for Hangman Stages ---
# The stages are ordered from 0 wrong guesses to 5.
stages = [
    # 0 wrong guesses (initial state)
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    # 1 wrong guess
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    # 2 wrong guesses
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    # 3 wrong guesses
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    # 4 wrong guesses
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    # 5 wrong guesses (final state)
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# -- Start of the Game --
clear_screen()

# -- Create List of Hangman with blanks "_" --
for i in range(numletters):
    hanglist.append("_")

while "_" in hanglist:
    # --- Display current game state at the start of each turn ---
    print("==============================================")
    print("   Welcome to Hangman! - Animal Edition   ")
    print("==============================================")
    print(stages[attempts])
    strhanglist = " ".join(hanglist)
    print(f"Word: {strhanglist}")
    print(f"Your guesses so far: {', '.join(guesslist)}")
    print("----------------------------------------------")
    
    # --- Get user input ---
    guess = input("Guess a letter: ").lower()
    clear_screen() # Clear the screen after the user enters their guess

    # --- Check for repeated guess ---
    if guess in guesslist:
        print(f"\n>> You already guessed '{guess}'. Try again.")
        continue # Skips the rest of this loop, asks for new letter

    guesslist.append(guess)

    # --- Check if the guess is correct or not ---
    if guess in randomword:
        # Correct guess: Update the hanglist with the letter
        for index, letter in enumerate(randomword):
            if letter == guess:
                hanglist[index] = guess
    else:
        # Incorrect guess: Increment attempts and check for game over
        attempts += 1
        if attempts >= 5:
            clear_screen()
            save_leaderboard(randomword, attempts, 'loss')
            print("\n==============================================")
            print(f"      GAME OVER! The word was '{randomword}'")
            print(stages[attempts]) # Show the final hangman
            print("==============================================")
            game_over = True
            break # Exit the main loop immediately


if not game_over:
    clear_screen()
    save_leaderboard(randomword, attempts, 'win')
    print("\n==============================================")
    print(f"      CONGRATULATIONS, YOU WON!")
    print(f" The word was '{randomword}', you got it with {attempts} wrong attempts.")
    print("==============================================")

# Display the leaderboard at the end of the game
display_leaderboard()
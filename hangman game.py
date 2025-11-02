import random
gamewords = ["owl","bunny","elephant","fox","camel","orangutan","zebra","antelope","baboon","cheetah","dolphin","elephant","flamingo","gorilla","hyena","iguana","jaguar","koala","lemur","meerkat","narwhal","ocelot","panda","quetzal","rhino","salamander","toucan"]
randomword = random.choice(gamewords)
numletters = len(randomword)
blankletters = "_ " * numletters
hanglist = []
attempts = 0
guesslist = []
game_over = False

# -- Start of the Game --
print("Welcome to hangman game!\nLet's start the Game with animal words")
print(f"\nThe word contains {numletters} letters {blankletters}\n")

# -- Create List of Hangman with blanks "_" --
for i in range(numletters):
    hanglist.append("_")


while "_" in hanglist:
    # -- First Guess --
    guess = input("Guess a letter: ").lower()

    # --- Check for repeated guess ---
    if guess in guesslist:
        print(f"You already guessed '{guess}'. Try again.")
        continue # Skips the rest of this loop, asks for new letter

    guesslist.append(guess)
    print(f"Your guesses: {guesslist}")

    # --- This inner loop runs ONLY if the guess is wrong ---
    while guess not in randomword:
        attempts += 1
        if attempts >= 5:
            print(f"Game over! You reached {attempts} attempts. The word was '{randomword}'")
            game_over = True # Set the flag
            break # Breaks the INNER loop
        else:
            print(f"Attempts: {attempts}. You have {5 - attempts} guesses left.")
            guess = input("Wrong guess! Guess another letter: ").lower()

            # --- Check for repeated guess (inside the loop) ---
            if guess in guesslist:
                 print(f"You already guessed '{guess}'.")
                 # Don't append, just let the 'while' loop check again
            else:
                 guesslist.append(guess)
                 print(f"Your guesses: {guesslist}")


    if game_over:
        break # Breaks the OUTER loop to end the game

    # --- This code only runs if the guess was correct ---
    # (or if it was the last guess that broke the inner loop)
    for index, letter in enumerate(randomword):
        if letter == guess:
            hanglist[index] = guess
    strhanglist = " ".join(hanglist)
    print(strhanglist)


if not game_over:
    print(f"You Won! The word was {randomword}, you got in {attempts} attempts")
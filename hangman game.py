import random
gamewords = ["owl","bunny","elephant","fox","cammel","orangutan","zebra"]
randomword = random.choice(gamewords)
numletters = len(randomword)
blankletters = "_ " * numletters
hanglist = []  
attempts = 0
guesslist = []
 

# -- Start of the Game --
print("Welcome to hangman game!\nLet's start the Game")
print(f"\nThe word contains {numletters} letters {blankletters}\n")

# -- Create List of Hangman with blanks "_" --
for i in range(numletters):
    hanglist.append("_")
    

while "_" in hanglist:
    # -- First Guess --
    guess = input("Guess a letter: ").lower()
    guesslist.append(guess)
    print(f"Your guesses: {guesslist}") 

    while guess not in randomword:
        attempts += 1
        if attempts >= 5:
            print(f"game over you reached {attempts} attempts")
            game_over = True
            break
        else:
            
            print(f"Attempts: {attempts}") 
            guess = input("Wrong guess! Guess another letter: ").lower()
            guesslist.append(guess)
            print(f"Your guesses: {guesslist}")
          

    for index, letter in enumerate(randomword):
        if letter == guess:
            hanglist[index] = guess
    strhanglist = " ".join(hanglist)
    print(strhanglist)

print(f"You Won! The word was {randomword}, you got in {attempts} attempts")


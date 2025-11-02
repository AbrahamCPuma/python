# Import necessary libraries. 'random' for card dealing and 'os' for clearing the screen.
import random
import os


#   Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#   Function to draw 2 cards it is only called at the beginning of the game
def draw2cards(player_cards, computer_cards,cards):
    for draws in range(2):
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

#   Function to calculate the score from the cards in the list, this needs to be called after every draw
def calculate(player_cards, computer_cards):
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)
    return player_score,computer_score

#   Function to check if there is a blackjack after each draw with the score parameters
def checkblackjack(player_score, computer_score,player_cards,computer_cards):
    #If player has blackjack player wins and starts a new game
    if player_score == 21:
        print("Player has Blackjack! You WIN")
        playagain()
    #If computer has blackjack player loses and starts a new game    
    elif computer_score == 21:
        print("Computer has Blackjack! You LOSE")
        playagain()
    else:
        # Check if player busts (score > 21).
        if player_score > 21:
            # If there is an Ace (11), change its value to 1.
            if 11 in player_cards:
                player_cards.remove(11)
                player_cards.append(1)
                player_score = sum(player_cards)
                
                # If score is still over 21, player loses.
                if player_score > 21:
                    print(f"player cards: {player_cards}")
                    print(f"Count: {player_score}\nBUSTED! You LOSE")
                    playagain()
                else:
                    return player_score, computer_score
            else:
                print(f"player cards: {player_cards}")
                print(f"Count: {player_score}\nBUSTED! You LOSE")
                playagain()
        # Check if computer busts.
        if computer_score > 21:
            if 11 in computer_cards:
                computer_cards.remove(11)
                computer_cards.append(1)
                computer_score = sum(computer_cards)
                
                if computer_score > 21:
                    print(f"player cards: {computer_cards}")
                    print(f"Count: {computer_score}\nComputer BUSTED! You WIN")
                    playagain()
                else:
                    return player_score, computer_score
            else:
                print(f"player cards: {player_cards}")
                print(f"Count: {player_score}\nComputer BUSTED! You WIN")
                playagain()
    return player_score, computer_score


                

#   Function to draw a card only if player wants to draw.
def drawcard(player_cards,computer_cards,cards):
    # Player draws one card.
    for draws in range(1):
        player_cards.append(random.choice(cards))
    player_score, computer_score = calculate(player_cards, computer_cards)
    player_score, computer_score= checkblackjack(player_score, computer_score,player_cards,computer_cards)
    return player_score

def drawcardcomputer(player_cards,computer_cards,cards):
    # Computer draws one card.
    for draws in range(1):
        computer_cards.append(random.choice(cards))
    player_score, computer_score = calculate(player_cards, computer_cards)
    player_score, computer_score = checkblackjack(player_score, computer_score,player_cards,computer_cards)
    return computer_score

# Function to ask the player if they want to play again.
def playagain():
    play_again = input("Do you want to play again? Y/N\t").lower()
    if play_again == "y":
        clear_screen()
    if play_again == "n":
        clear_screen()
        exit()

# Main game loop.
while True:
    # Define the deck of cards for each new game.
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    playagain()

    # Initialize empty hands for player and computer.
    player_cards = []
    computer_cards = []
    play = input("Welcome to Blackjack!, Do you want to play? Y/N\t").lower()
    if play == "y":
        clear_screen()
    if play == "n":
        clear_screen()
        exit() # This will terminate the entire program

    # Deal initial cards and calculate scores.
    draw2cards(player_cards, computer_cards,cards)
    player_score, computer_score = calculate(player_cards, computer_cards)
    checkblackjack(player_score, computer_score,player_cards,computer_cards)
    
    # Display initial hands (hiding computer's second card).
    print(f"player cards: {player_cards}")
    print(f"computer cards: [{computer_cards[0]}, ?]")
    print(f"player = {player_score}, computer = {computer_score}\n")

    # Player's turn loop.
    while player_score < 21:    
        draw = input("Do you want to draw a card? Y/N\t").lower()
        if draw == "y":
            player_score = drawcard(player_cards,computer_cards,cards)
            print(f"player cards: {player_cards}")
            print(f"computer cards: [{computer_cards[0]}, ?]")
            print(f"player = {player_score}, computer = {computer_score}\n")
            
        # If player chooses to stand.
        if draw == "n":
            # Computer hits if its score is 16 or less.
            if computer_score > 16:
                computer_score = drawcardcomputer(player_cards,computer_cards,cards)
            print(f"player = {player_score}, computer = {computer_score}\n")
            # Compare final scores to determine the winner.
            if player_score > computer_score:
                print("You WIN")
                
            elif player_score < computer_score:
                print("You LOSE")
            
            else:
                print("You DRAW")
                break
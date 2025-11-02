# Import necessary libraries. 'random' for card dealing and 'os' for clearing the screen.
import random
import os

def deal_cards():
    """Returns a random card from the deck."""
    # The deck includes face cards (10) and an Ace (11).
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # Check for a Blackjack (a score of 21 with exactly two cards).
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # If the score is over 21 and there's an Ace (11), change the Ace's value to 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(p_score, c_score):
    """Compares the player's and computer's scores to determine the winner."""
    if p_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif p_score == 0:
        return "Win with a Blackjack"
    elif p_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif p_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    """Main function to run a single game of Blackjack."""
    # Initialize empty hands for the player and computer.
    player_cards = []
    computer_cards = []
    computer_score = -1
    player_score = -1
    is_game_over = False

    # Deal two initial cards to both the player and the computer.
    for i in range(2):
        player_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    # Main game loop for the player's turn.
    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # The game ends immediately if someone has Blackjack or the player busts.
        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True

        else:
            player_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if player_should_deal == "y":
                player_cards.append(deal_cards())
            
            else:
                is_game_over = True

    # Computer's turn: it must hit until its score is 17 or more.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    # Display the final hands and scores.
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

# Main game loop to ask the player if they want to play again.
while input("Do you want to play a Blackjack game? Y/N\t").lower():
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()
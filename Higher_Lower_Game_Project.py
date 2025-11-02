import random
import os
from data_higher_lower_game import data

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def compare(guess, followers_a, followers_b):
    """Checks followers against user's guess.
    Returns True if they got it right, False if they got it wrong."""
    if followers_a > followers_b:
        return guess == "a"
    else:
        return guess == "b"

def game():
    # Create a copy of the data to use as a pool of available accounts
    available_data = data.copy()
    score = 0
    game_should_continue = True

    # Pick the first account and remove it from the available pool
    pick_a = random.choice(available_data)
    available_data.remove(pick_a)

    while game_should_continue:
        # Pick the second account and remove it from the pool
        pick_b = random.choice(available_data)
        available_data.remove(pick_b)

        print(f"Compare A:  {pick_a["name"]}, a {pick_a["description"]}, from {pick_a["country"]}.")
        print("\n\nVS\n\n")
        print(f"Compare B:  {pick_b["name"]}, a {pick_b["description"]}, from {pick_b["country"]}.")
        guess = input("\nWho has more followers? Type 'A' or 'B':\t").lower()

        is_correct = compare(guess, pick_a["follower_count"], pick_b["follower_count"])

        clear_screen()
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
            # The winner becomes the next 'A'
            if pick_b['follower_count'] > pick_a['follower_count']:
                pick_a = pick_b
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

        if not available_data: # Check if the pool of accounts is empty
            game_should_continue = False
            print(f"You've compared everyone! You win! Final score: {score}")

game()
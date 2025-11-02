import os

bidders = {}
continue_program = True

def find_highest_bidder(bidders_data):
    """
    Finds the person with the highest bid in a dictionary of bidders.
    Returns the winner's name and their bid amount.
    """
    if not bidders_data: # Handle case where there are no bidders
        return None, 0

    highest_amount = 0
    winner = ""
    for bidder, bid_amount in bidders_data.items():
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidder
    return winner, highest_amount


print("Welcome to Bidders.com you entered an auction!\n")

while continue_program:
    name = input("What is your name?\t")
    # Loop to ensure a valid bid is entered
    while True:
        try:
            bid_input = input("What is your bid?\t$")
            bid = int(bid_input)
            break # Exit loop if input is a valid integer
        except ValueError:
            print("Invalid input. Please enter a whole number for your bid.")
    bidders[name] = bid
    next_bidder = input("Is there another bidder? Y/N\t").lower()

    if next_bidder == "y":
        os.system('cls' if os.name =='nt' else 'clear')
    if next_bidder == "n":
        continue_program = False

# --- Find and Announce Winner ---
winner_name, winning_bid = find_highest_bidder(bidders_data=bidders)

os.system('cls' if os.name =='nt' else 'clear')
if winner_name:
    print(f"The winner is {winner_name} with a bid of ${winning_bid}!")
else:
    print("There were no bidders in the auction.")
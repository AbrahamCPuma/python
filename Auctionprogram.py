# Import the 'os' module to interact with the operating system, used here for clearing the screen.
import os

# Initialize an empty dictionary to store bidder names and their bids.
bidders = {}
# A flag to control the main loop of the program.
continue_program = True

def find_highest_bidder(bidders_data):
    """Finds the highest bid in a dictionary of bidders."""
    if not bidders_data: # Handle case where there are no bidders
        return None, 0

    highest_amount = 0
    winner = ""
    for bidder, bid_amount in bidders_data.items():
        if bid_amount > highest_amount:
            # If the current bidder's amount is higher, update the highest amount and winner.
            highest_amount = bid_amount
            winner = bidder
    return winner, highest_amount


# Display a welcome message for the auction.
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
    # Add the bidder's name and bid to the dictionary.
    bidders[name] = bid
    # Ask if there are more bidders to continue or end the loop.
    next_bidder = input("Is there another bidder? Y/N\t").lower()

    if next_bidder == "y":
        # Clear the screen for the next bidder.
        os.system('cls' if os.name =='nt' else 'clear')
    if next_bidder == "n":
        # Set the flag to false to exit the while loop.
        continue_program = False

# --- Find and Announce Winner ---
# Call the function to determine the winner from the collected bids.
winner_name, winning_bid = find_highest_bidder(bidders_data=bidders)

# Clear the screen before announcing the winner.
os.system('cls' if os.name =='nt' else 'clear')
if winner_name:
    print(f"The winner is {winner_name} with a bid of ${winning_bid}!")
else:
    print("There were no bidders in the auction.")
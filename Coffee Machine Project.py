MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "5 cents": 0.05,
    "10 cents": 0.10,
    "25 cents": 0.25,
    "50 cents": 0.50,
}

def prompt():
    """
    Asks the user what they would like.
    Returns the user's choice as a string.
    """
    while True:
        promptinput = input("What would you like? (espresso/latte/cappuccino)\t").lower()

        if promptinput == "report":
            report()
        # ADDED "off" switch to stop the machine
        elif promptinput == "off":
            return "off"
        elif promptinput in ["espresso", "latte", "cappuccino"]:
            return promptinput
        else:
            print("Sorry, I don't understand that choice. Please try again.")


def report():
    """Prints a report of the current resources."""
    print("--- Current Resources ---")
    for key, value in resources.items():
        # Added units for clarity
        if key == "coffee":
            print(f"{key.title()}: {value}g")
        elif key == "water" or key == "milk":
            print(f"{key.title()}: {value}ml")
    print("-------------------------")


def check_resources(beverage):
    """
    Checks if there are sufficient resources to make the beverage.
    Returns True if resources are sufficient, False if not.
    """
    ingredients_needed = MENU[beverage]["ingredients"]
    for item_key, needed_amount in ingredients_needed.items():
        current_amount = resources[item_key]
        
        if current_amount < needed_amount:
            print(f"Sorry, there is not enough {item_key}.")
            return False
    return True


def process_payment():
    """
    Asks the user to insert coins and calculates the total value.
    Returns the total amount of money inserted as a float.
    Includes error handling for non-numeric input.
    """
    print("Please insert coins.")
    total_money = 0
    for coin_name, coin_value in coins.items():
        try:
            # Ask for coins and convert to int in one step
            num_coins = int(input(f"How many {coin_name}?: "))
            total_money += (num_coins * coin_value)
        except ValueError:
            # This 'except' block catches errors if user types "one" instead of 1
            print("Invalid input. Only numbers are allowed.")
            # We can just assume 0 coins were entered for this type
            total_money += 0 
            
    print(f"Money inserted: ${total_money:.2f}")
    return total_money


def is_transaction_successful(money_inserted, beverage_cost):
    """
    Checks if the payment is sufficient.
    If payment is high, calculates and prints change.
    If payment is low, prints error and refunds money.
    Returns True if payment is sufficient, False if not.
    """
    if money_inserted >= beverage_cost:
        change = money_inserted - beverage_cost
        if change > 0:
            print(f"Your change is: ${change:.2f}")
        return True
    else:
        missing_amount = beverage_cost - money_inserted
        print(f"Sorry, Not enough money. You are missing ${missing_amount:.2f} - Money refunded!")
        return False


def reduce_resources(beverage):
    """
    Deducts the ingredients used for the beverage
    from the global 'resources' dictionary.
    """
    ingredients_needed = MENU[beverage]["ingredients"]
    for item, amount in ingredients_needed.items():
        resources[item] -= amount


# --- Main Program ---
print("\nWelcome to the coffee machine!\n")
is_on = True

while is_on:
    # 1. Ask user for choice (handles "report" and "off" itself)
    choice = prompt()
    
    if choice == "off":
        # 2. Check for "off" command
        is_on = False
        print("Turning off the machine. Goodbye!")
        
    elif choice in MENU: 
        # 3. Check resources
        if check_resources(choice):
            
            # 4. Process payment (this function now asks for coins *and* returns total)
            cost_of_drink = MENU[choice]["cost"]
            money_paid = process_payment()
            
            # 5. Check if transaction was successful
            if is_transaction_successful(money_paid, cost_of_drink):
                
                # 6. Make coffee and reduce resources
                print(f"Making your {choice}. Enjoy!")
                reduce_resources(choice)

import streamlit as st

# --- Constants (Same as your file) ---
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

coins = {
    "5 cents": 0.05,
    "10 cents": 0.10,
    "25 cents": 0.25,
    "50 cents": 0.50,
}

# --- State Management (The most important part!) ---
# This dictionary holds our resources.
# We must use 'st.session_state' to make sure the
# 'resources' are not reset on every button click.

if 'resources' not in st.session_state:
    st.session_state.resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

# --- Functions (Almost identical to yours, just modified for Streamlit) ---

def check_resources(beverage):
    """
    Checks if there are sufficient resources.
    Returns True if sufficient, False if not.
    """
    ingredients_needed = MENU[beverage]["ingredients"]
    for item_key, needed_amount in ingredients_needed.items():
        # Read from session_state
        current_amount = st.session_state.resources[item_key]
        
        if current_amount < needed_amount:
            # Use st.error() instead of print()
            st.error(f"Sorry, there is not enough {item_key}.")
            return False
    return True

def reduce_resources(beverage):
    """Deducts ingredients from the resources in session_state."""
    ingredients_needed = MENU[beverage]["ingredients"]
    for item, amount in ingredients_needed.items():
        # Modify session_state
        st.session_state.resources[item] -= amount

# --- The Main Web App UI (User Interface) ---

st.title("☕ Welcome to the Coffee Machine!")

# --- 1. Drink Selection ---
choice = st.selectbox(
    "What would you like?",
    ("espresso", "latte", "cappuccino"),
    index=None, # Makes it show a placeholder
    placeholder="Select a drink...",
)

# --- 2. Coin Input ---
st.subheader("Please Insert Coins")
col1, col2 = st.columns(2) # Organize in columns

with col1:
    cents5 = st.number_input("How many 5 cents?", min_value=0, step=1)
    cents10 = st.number_input("How many 10 cents?", min_value=0, step=1)
with col2:
    cents25 = st.number_input("How many 25 cents?", min_value=0, step=1)
    cents50 = st.number_input("How many 50 cents?", min_value=0, step=1)

# --- 3. "Make Coffee" Button and Logic ---
if st.button("Make Coffee!", type="primary"):
    if choice is None:
        st.warning("Please select a drink first.")
    else:
        # Check if resources are sufficient
        if check_resources(choice):
            
            # --- Check Money (Logic from your function) ---
            total_money = (cents5 * coins["5 cents"]) + \
                          (cents10 * coins["10 cents"]) + \
                          (cents25 * coins["25 cents"]) + \
                          (cents50 * coins["50 cents"])
            
            st.write(f"Money inserted: ${total_money:.2f}")
            
            cost_of_drink = MENU[choice]["cost"]
            
            if total_money >= cost_of_drink:
                # Give change
                change = total_money - cost_of_drink
                if change > 0:
                    st.success(f"Your change is: ${change:.2f}")
                
                # Make the coffee
                st.success(f"Making your {choice}. Enjoy!")
                st.balloons() # Fun celebration!
                
                # Reduce resources
                reduce_resources(choice)
                
            else:
                missing = cost_of_drink - total_money
                st.error(f"Sorry, Not enough money. You are missing ${missing:.2f} - Money refunded!")

# --- 4. Admin Report in the Sidebar ---
st.sidebar.title("Admin Panel")
if st.sidebar.button("Show Report"):
    st.sidebar.subheader("Current Resources")
    # Read from session_state
    for key, value in st.session_state.resources.items():
        st.sidebar.write(f"{key.title()}: {value}")

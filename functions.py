# Define a function named 'greetings' that takes one argument, 'name'.
def greetings(name):
    print(f"\nHello {name}")
    print(f"How are you? {name}")
    print(f"Good bye {name}")
# Get the user's name as input.
name = input("What is your name?\n\n")
# Ask the user if they want a greeting.
greet = input("Do you want a greeting? Y/N\n\n").lower()
if greet == "y":
    # Call the 'greetings' function, passing the user's name to it.
    greetings(name)

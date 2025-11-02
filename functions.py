def greetings(name):
    print(f"\nHello {name}")
    print(f"How are you? {name}")
    print(f"Good bye {name}")
name = input("What is your name?\n\n")
greet = input("Do you want a greeting? Y/N\n\n").lower()
if greet == "y":
    greetings(name)

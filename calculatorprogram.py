import os

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
operations = {
    "+" :add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    """Main function to run the calculator logic."""
    clear_screen()
    try:
        n1 = float(input("What is the first number?\t"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        
        input_operation = input("What operation do you want to perform?\t")
        if input_operation not in operations:
            print("Invalid operation. Please choose from the list above.")
            continue

        while True:
            try:
                n2 = float(input("What is the next number?\t"))
                break # Exit the inner loop if the input is a valid number
            except ValueError:
                print("Invalid input. Please enter a number and try again.")
                # The loop will repeat, asking only for n2 again.

        calculation_function = operations[input_operation]
        result = calculation_function(n1, n2)

        print(f"{n1} {input_operation} {n2} = {result}")

        if isinstance(result, str): # Check if an error message was returned
            break

        run_again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if run_again == 'y':
            n1 = result
        else:
            should_continue = False
            break

if __name__ == "__main__":
    while True:
        calculator()

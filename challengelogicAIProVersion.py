# --- CONFIGURATION & CONSTANTS ---
# Pros often put configurable values at the top as constants.
# This makes them easy to find and change without digging through the code.
# These constants define the business rules for user registration.
MIN_USERNAME_LENGTH = 6
MIN_PASSWORD_LENGTH = 8
MIN_AGE = 18
VALID_ROLES = ['admin', 'moderator']
BANNED_USERS = ['abraham94', 'abraham95']

# --- VALIDATION FUNCTIONS ---
# Each function has one specific job: to validate one piece of data.
# They return True or False, which is clear and easy to test.

def validate_username(username):
    """Checks if the username is valid."""
    return len(username) >= MIN_USERNAME_LENGTH and ' ' not in username

def validate_age(age_input):
    """Checks if the age is a number and meets the minimum requirement."""
    return age_input.isdigit() and int(age_input) >= MIN_AGE

def validate_password(password):
    """Checks if the password is valid."""
    return len(password) >= MIN_PASSWORD_LENGTH and ' ' not in password

def validate_email(email):
    """Checks if the email appears to be valid."""
    # Note: Real-world email validation is much more complex, but this is good for our purpose.
    return '@' in email and email.endswith('.com')

def validate_role(role):
    """Checks if the role is one of the allowed roles."""
    return role.lower() in VALID_ROLES

# --- MAIN APPLICATION LOGIC ---

def main():
    """Main function to run the user registration and validation process."""
    print('-----User Registration-----\n')

    # 1. Get User Input
    user_name = input('Write your user name:\t')
    age_input = input('Write your age:\t')
    password = input('Write your password:\t')
    email = input('Write your email:\t')
    role = input('Write your role (Admin/Moderator):\t')

    # 2. Perform Initial Checks (e.g., Banned User)
    # This is an "early exit" or "guard clause" pattern.
    if user_name in BANNED_USERS:
        print(f'\n❌ Access Denied: The user name "{user_name}" is banned.')
        return # Exit the function early if the user is banned

    # 3. Run All Validations
    # We store the results of our validation functions in a clear, readable way.
    validations = {
        "Username": (validate_username(user_name), f"Must be at least {MIN_USERNAME_LENGTH} characters and contain no spaces."),
        "Age": (validate_age(age_input), f"Must be a number and at least {MIN_AGE} years old."),
        "Password": (validate_password(password), f"Must be at least {MIN_PASSWORD_LENGTH} characters and contain no spaces."),
        "Email": (validate_email(email), "Must be a valid email ending in .com."),
        "Role": (validate_role(role), f"Must be one of the following: {', '.join(VALID_ROLES)}.")
    }

    # 4. Report Results
    print('\n-----Validation Results-----\n')

    # Collect all validation failures into a list of error messages.
    errors = []
    for field, (is_valid, message) in validations.items():
        if not is_valid:
            errors.append(f"• {field}: {message}")

    # Display the final outcome
    if not errors:
        # If the errors list is empty, registration is successful.
        print(f"✔️ Welcome, {user_name}! All details are valid. Registration successful.")
    else:
        print(f"Hello, {user_name}. Please correct the following issues:")
        for error in errors:
            print(f"  {error}")

# --- SCRIPT ENTRY POINT ---
# This is a standard Python convention. It means "run the main() function
# only when this script is executed directly."
if __name__ == "__main__":
    main()

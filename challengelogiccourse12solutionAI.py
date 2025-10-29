print('-----Initialize-----\n')
user_name = input('Write your user name:\t')
age_input = input('\nWrite your age:\t')
pwd = input('\nWrite your password:\t')
email = input('\nWrite your email:\t')
role = input('\nWrite your role:\t')

banned_list = ['abraham94','abraham95']

# --- VALIDATIONS ---
# It's good practice to set default validation results to False.
# This way, they only become True if they pass all checks.
is_age_valid = False
is_username_valid = False
is_password_valid = False
is_email_valid = False

# --- Age Validation ---
# First, check if the input for age consists of digits.
# This prevents the program from crashing if the user enters text.
if age_input.isdigit():
    # If it's a number, convert it to an integer and check if it's 18 or over.
    age = int(age_input)
    if age >= 18:
        is_age_valid = True

# --- User Name Validation ---
# A single, clear validation for the username.
# A non-empty string is "truthy" in Python, so `if user_name:` checks if it's not empty.
if user_name and len(user_name) > 5 and ' ' not in user_name:
    is_username_valid = True

# --- Password Validation ---
# Your original logic was already good and clear!
if len(pwd) >= 8 and ' ' not in pwd:
    is_password_valid = True

# --- Email Validation ---
# Simplified the check. `if email:` handles the empty string case.
if email and '@' in email and email.endswith('.com'):
    is_email_valid = True


# --- RESULTS ---
print('\n-----Results-----\n')

# First, check the banned list. This is a great first step.
if user_name in banned_list:
    print(f'The user name "{user_name}" is BANNED.\n')
else:
    # Now, check each validation result.

    # Combined username and age check for the initial message
    if is_username_valid and is_age_valid:
        print(f'Welcome, {user_name}! Your registration details are being processed.')
    else:
        print(f'Hello, {user_name}. There are some issues with your registration details.')

    # Check username
    if is_username_valid:
        print('✔️ Your user name is accepted.')
    else:
        print(f'❌ Your user name "{user_name}" is not valid. It must be longer than 5 characters and contain no spaces.')

    # Check age
    if is_age_valid:
        print(f'✔️ Your age ({age}) is valid.')
    else:
        print(f'❌ Your age "{age_input}" is not valid. You must be 18 or older, and enter a valid number.')

    # Check password
    if is_password_valid:
        print('✔️ Your password is accepted.')
    else:
        print(f'❌ Your password is not valid. It must be at least 8 characters long and contain no spaces.')

    # Check email
    if is_email_valid:
        print('✔️ Your email is accepted.')
    else:
        print(f'❌ Your email "{email}" is not valid. It must contain "@" and end with ".com".')

    # Check role
    if role.lower() == 'admin':
        print(f'✔️ You registered as an Admin.')
    elif role.lower() == 'moderator':
        print(f'✔️ You registered as a Moderator.')
    else:
        print(f'❌ Your role is not valid. Please enter "Admin" or "Moderator".')


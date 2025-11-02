# --- CONFIGURATION & CONSTANTS ---
# These are our business rules for the data pipeline.
# They define what is considered valid data.
MIN_USERNAME_LENGTH = 6
MIN_PASSWORD_LENGTH = 8
MIN_AGE = 18
VALID_ROLES = ['admin', 'moderator', 'user']
BANNED_USERS = ['abraham94', 'abraham95']

# --- VALIDATION FUNCTIONS (The "Transform" step) ---
# These functions are our reusable cleaning/validation tools. Each has a single responsibility.

def validate_username(username):
    """Checks if the username is valid."""
    return isinstance(username, str) and len(username) >= MIN_USERNAME_LENGTH and ' ' not in username

def validate_age(age):
    """Checks if the age is a number and meets the minimum requirement."""
    return isinstance(age, int) and age >= MIN_AGE

def validate_email(email):
    """Checks if the email appears to be valid."""
    return isinstance(email, str) and '@' in email and email.endswith('.com')

def validate_role(role):
    """Checks if the role is one of the allowed roles."""
    return isinstance(role, str) and role.lower() in VALID_ROLES

# --- PIPELINE ORCHESTRATOR ---

def run_user_processing_pipeline(raw_records):
    """
    This function acts as our main pipeline.
    It takes raw data, processes it, and separates it into clean and rejected buckets.
    """
    clean_records = []
    rejected_records = []

    print(f"--- Starting pipeline: processing {len(raw_records)} records ---")

    # This loop is the core of the pipeline, processing one record at a time.
    for record in raw_records:
        # For each record, start with an empty list of errors.
        errors = []
        user_name = record.get('username', '')

        # 1. Initial checks (like a gatekeeper)
        if user_name in BANNED_USERS:
            errors.append("User is on the banned list")
        
        # 2. Field-level validation using the helper functions.
        if not validate_username(user_name):
            errors.append(f"Invalid username: '{user_name}'")
        if not validate_age(record.get('age')):
            errors.append(f"Invalid age: '{record.get('age')}'")
        if not validate_email(record.get('email')):
            errors.append(f"Invalid email: '{record.get('email')}'")
        if not validate_role(record.get('role')):
            errors.append(f"Invalid role: '{record.get('role')}'")

        # 3. Route the data based on validation results
        # If there are no errors, the record is clean. Otherwise, it's rejected.
        if not errors:
            clean_records.append(record)
        else:
            # In a real pipeline, we'd log these errors. Here, we add them to the record.
            record['rejection_reasons'] = errors
            rejected_records.append(record)

    print("--- Pipeline finished ---")
    return clean_records, rejected_records

# --- SCRIPT ENTRY POINT ---
if __name__ == "__main__":
    # 1. EXTRACT: In a real pipeline, this data would come from a file, database, or API.
    # Here, we simulate it with a list of dictionaries.
    source_data = [ # This is our raw, unprocessed data.
        {'username': 'testuser1', 'age': 30, 'email': 'test1@example.com', 'role': 'Admin'},
        {'username': 'bad', 'age': 25, 'email': 'test2@example.com', 'role': 'User'}, # Bad username
        {'username': 'testuser3', 'age': 17, 'email': 'test3@example.com', 'role': 'User'}, # Bad age
        {'username': 'testuser4', 'age': 40, 'email': 'test4@invalid', 'role': 'Moderator'}, # Bad email
        {'username': 'abraham95', 'age': 28, 'email': 'banned@example.com', 'role': 'User'}, # Banned user
        {'username': 'testuser5', 'age': 'fifty', 'email': 'test5@example.com', 'role': 'Guest'}, # Bad age type and role
        {'username': 'testuser6', 'age': 50, 'email': 'test6@example.com', 'role': 'user'},
    ]

    # 2. TRANSFORM: Run the main processing function to clean and validate the data.
    valid_users, invalid_users = run_user_processing_pipeline(source_data)

    # 3. LOAD: In a real pipeline, this data would be written to a data warehouse,
    # a database, or another file. Here, we just print the results.
    print(f"\n--- Loading Results ---")
    print(f"\n✅ {len(valid_users)} Clean Records to be loaded into production system:")
    for user in valid_users:
        print(f"  - {user}")

    print(f"\n❌ {len(invalid_users)} Rejected Records to be sent to quarantine for review:")
    for user in invalid_users:
        print(f"  - {user}")

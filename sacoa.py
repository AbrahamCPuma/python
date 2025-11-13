import requests
import sys

# --- PLEASE CONFIGURE THESE VALUES ---

# !!! IMPORTANT: Replace with your actual API base URL
# It probably looks something like "https://api.yourcompany.com"
BASE_URL = "https://dev.sacoacard.com:33033/"

# Credentials for the /login endpoint
LOGIN_USER = "marcoscavazquez"
LOGIN_PASS = "KnowOutCinemex1!"
COMPUTER_ID = "1"

# Parameters for the /games/getGameName endpoint
# These values are from your first screenshot
POS_ID = 1
EXT_EMP_ID = 1
GAME_ID_TO_GET = 10

# --- END OF CONFIGURATION ---


def get_auth_token(base_url, user, password, computer_id):
    """
    Authenticates with the /login endpoint to get a token and empId.
    """
    login_url = f"{base_url}/login"
    login_payload = {
        "user": user,
        "pass": password,
        "computerId": computer_id
    }

    print(f"Attempting login to {login_url}...")
    try:
        # Make the POST request
        response = requests.post(login_url, json=login_payload)
        
        # This will raise an error for bad responses (4xx or 5xx)
        response.raise_for_status() 

        data = response.json()

        # Check for logical success based on the API response structure
        if data.get("statusCode") == 200 and data.get("body", {}).get("authorized"):
            token = data["body"].get("token")
            emp_id = data["body"].get("empId")
            
            if token and emp_id:
                print("Login SUCCESSFUL.")
                return token, emp_id
            else:
                print("Login FAILED: 'token' or 'empId' missing from response body.")
                return None, None
        else:
            print(f"Login FAILED: API reported an error (statusCode={data.get('statusCode')}).")
            print(f"Response: {data}")
            return None, None

    except requests.exceptions.RequestException as e:
        print(f"Login FAILED: An HTTP error occurred: {e}", file=sys.stderr)
        return None, None
    except Exception as e:
        print(f"Login FAILED: An unexpected error occurred: {e}", file=sys.stderr)
        return None, None

def get_game_name(base_url, token, emp_id, pos_id, ext_emp_id, game_id):
    """
    Fetches the game name using the provided auth token and empId.
    """
    game_url = f"{base_url}/games/getGameName"
    
    # Note: Your getGameName example shows empId as a number (1),
    # but your login response shows it as a string ("1").
    # We will try to cast it to an int to match the example.
    try:
        emp_id_for_game = int(emp_id)
    except (ValueError, TypeError):
        print(f"Warning: empId from login ('{emp_id}') was not a number. Using as-is.")
        emp_id_for_game = emp_id # Use the string if it's not an int

    game_payload = {
        "posId": pos_id,
        "empId": emp_id_for_game,
        "token": token,
        "extEmpId": ext_emp_id,
        "gameId": game_id
    }

    print(f"\nAttempting to get game name from {game_url}...")
    try:
        response = requests.post(game_url, json=game_payload)
        response.raise_for_status() # Check for HTTP errors

        data = response.json()

        if data.get("statusCode") == 200 and data.get("body"):
            # The body is a list, so we get the first item
            game_info = data["body"][0] 
            game_name = game_info.get("Name")
            print(f"API call SUCCESSFUL.")
            return game_name
        else:
            print(f"Get game name FAILED: API reported an error (statusCode={data.get('statusCode')}).")
            print(f"Response: {data}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Get game name FAILED: An HTTP error occurred: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Get game name FAILED: An unexpected error occurred: {e}", file=sys.stderr)
        return None

# Main part of the script
if __name__ == "__main__":
    # Step 1: Authenticate
    auth_token, employee_id = get_auth_token(
        BASE_URL, 
        LOGIN_USER, 
        LOGIN_PASS, 
        COMPUTER_ID
    )

    # Step 2: If login is successful, get the game name
    if auth_token and employee_id:
        
        game_name = get_game_name(
            BASE_URL,
            auth_token,
            employee_id,
            POS_ID,
            EXT_EMP_ID,
            GAME_ID_TO_GET
        )

        if game_name:
            print(f"\n--- RESULT ---")
            print(f"The name for GameID {GAME_ID_TO_GET} is: {game_name}")
        else:
            print("\nCould not retrieve the game name.")
    else:
        print("\nCannot proceed to get game name without successful login.")
# Import the regular expression module.
import re

string = '968-Maria, ( D@t@ Engineer );; 27y  '
# --- A more robust method using Regular Expressions ---

# 1. Define a pattern to find the name, role, and age.
#    - ([a-zA-Z]+): Captures one or more letters (the name).
#    - \(\s*(.*?)\s*\): Captures anything inside parentheses (the role), ignoring surrounding spaces.
#    - (\d+): Captures one or more digits (the age).
pattern = re.compile(r'([a-zA-Z]+).*?\(\s*(.*?)\s*\).*?(\d+)')

# 2. Search the original string for this pattern.
match = pattern.search(string)

# 3. Extract the captured groups and clean them up.
if match:
    # The captured groups are indexed from 1.
    name = match.group(1).strip()
    role = match.group(2).strip().lower().replace('@', 'a')
    age = match.group(3).strip()

    # 4. Build the final string using an f-string for better readability.
    stringcleaned = f"name: {name} | role: {role} | age: {age}"
    print(stringcleaned)
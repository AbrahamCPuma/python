# Import the 'math' and 'random' modules.
import math, random
'''
price = 35.45989865

# round() function to round a number to a specified number of decimal places.
print(round(price,2))

# random.random() returns a random float between 0.0 and 1.0.
print(random.random())

# random.randint() returns a random integer within a specified range.
print(random.randint(1,6))

x = 7

# is_integer() checks if a float is a whole number.
print(price.is_integer())'''

# Generate a random integer between 1 and 100.
number = random.randint(1,100)
print(number)
# Use the modulo operator (%) to check if the number is even or odd.
if number%2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')
 
# Example variables for registration checks.
email = 'ab@gmail.com'
phone = '0176-123456'
username = 'abc94'
# Allows registrations
# If any field is filled
# The all() function returns True if all items in an iterable are true.
# Here, it checks if email, phone, and username strings are not empty.
print(all([email, phone, username]))

# The isinstance() function checks if an object is an instance of a specified class.
print(isinstance(123, int))

# Example of checking if a value is within a specific range.
age = 40
print(18 <= age <= 30)
# Example strings for demonstration.
phone = 'alergi1cs-'

phone2 = '48-654-16548'

# The isalpha() method checks if all characters in the string are alphabetic.
print(phone.isalpha())
# The find() method returns the index of the first occurrence of a substring.
# String slicing is used here to get the part of the string after the first hyphen.
print(phone2[phone2.find('-')+1:])

print(phone.find('-')) 
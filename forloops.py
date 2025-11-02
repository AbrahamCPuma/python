# A simple for loop to print the multiplication table for the number 7.
number = 7

for i in range(1,11):
    result = number * i
    print(f'{number} X {1} = {result}')

# A loop to build and print a triangle of stars.
ss =''
for star in range(0,6):
    ss += '*'
    print(ss)
    
# A loop to iterate over a list of items and print each one.
items = [1,2,3,4,7]
for i in items:
    print(i)
    
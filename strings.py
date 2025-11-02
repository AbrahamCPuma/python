# The initial messy string.
string = '968-Maria, ( D@t@ Engineer );; 27y  '
# A chain of string methods to clean the data in multiple steps.
string =string.lower().replace('@','a').strip().replace('968-','name: ').replace('(','|').replace(')','|').replace(',','').replace(';','').replace('y','')
# Slicing the cleaned string into parts.
string1 = string[0:14]
string2 = string[14:-2]
string3 = string[-2:]
print(string)

# Concatenating the parts back together into a final, formatted string.
stringcleaned = string1 + 'role: '+ string2 + 'age: ' + string3
print(stringcleaned)
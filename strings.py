string = '968-Maria, ( D@t@ Engineer );; 27y  '
string =string.lower().replace('@','a').strip().replace('968-','name: ').replace('(','|').replace(')','|').replace(',','').replace(';','').replace('y','')
string1 = string[0:14]
string2 = string[14:-2]
string3 = string[-2:]
print(string)

stringcleaned = string1 + 'role: '+ string2 + 'age: ' + string3
print(stringcleaned)
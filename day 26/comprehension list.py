list = [1,2,3]
new_list = [n + 1 for n in list ]
print(list)
print(new_list)

name = "Angela"
new_name = [n for n in name]
print(new_name)

rang = range(1,5)
new_rang = [n*2 for n in range(1,5)]
print(new_rang)

names = ["angela", "alex" , "yahir", "ana", "tony", "bahaa"]
short_names = [name.upper() for name in names if len(name) < 5]
print(short_names)
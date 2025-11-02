# A dictionary is a collection of key-value pairs.
Dict = {"name" : "Abraham",
        "age" : "30",
        "country" : "Mexico",
        }

# You can add a new key-value pair to a dictionary.
Dict["city"] = "CDMX"

# You can loop through the keys of a dictionary.
for i in Dict:
    print(f"{i} : {Dict[i]}")


# Another example of a dictionary.
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "United Kingdom": "London",
}

# A dictionary where the values are lists. This is a nested data structure.
travel_log = {
    "France" : ["paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}

# A list that contains another list.
nested_list = ["A", "B", ["C", "D"]]

# Accessing elements in nested data structures.
print(nested_list[2][1])
print(travel_log["France"])

# Using the .index() method to find the position of an item in a list.
index = travel_log["France"].index("paris")
print(travel_log["France"][index])

# A more complex nested dictionary where values are themselves dictionaries.
travel_log2 = {
    "France" : {
        "num_time_visited" : 8,
        "cities_visited" : ["paris", "Lille", "Dijon"],
    },
    "Germany" : {
        "num_time_visited" : 5,
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
    },
}

# Accessing a deeply nested element.
print(travel_log2["Germany"]["cities_visited"][2])
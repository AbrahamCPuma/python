Dict = {"name" : "Abraham",
        "age" : "30",
        "country" : "Mexico",
        }

Dict["city"] = "CDMX"

for i in Dict:
    print(f"{i} : {Dict[i]}")


capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "United Kingdom": "London",
}

travel_log = {
    "France" : ["paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])
print(travel_log["France"])

index = travel_log["France"].index("paris")
print(travel_log["France"][index])

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

print(travel_log2["Germany"]["cities_visited"][2])
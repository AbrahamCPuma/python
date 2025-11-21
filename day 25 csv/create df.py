import pandas as pd

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76,56,65]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("./learningbasicpy/day 25 csv/new_data.csv")
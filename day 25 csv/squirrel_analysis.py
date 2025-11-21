import pandas as pd
df = pd.read_csv("D:/python/learningbasicpy/day 25 csv/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


gray_count = len(df[df["Primary Fur Color"] == "Gray"])
red_count = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_count = len(df[df["Primary Fur Color"] == "Black"])

dict_analysis = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_count,red_count,black_count]
}

new_df = pd.DataFrame(dict_analysis)
print(new_df)
#new_df.to_csv("./learningbasicpy/day 25 csv/squirrel_count.csv")
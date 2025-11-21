
import pandas as pd

df = pd.read_csv("D:/python/learningbasicpy/day 25 csv/weather_data.csv")
print(df["temp"])
temp_list = df["temp"].to_list()

print(round(sum(temp_list)/len(temp_list),2))
monday = df[df.day == "Monday"]
print(monday.temp * 9/5 + 32)
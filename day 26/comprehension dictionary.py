# new_dict = {new_key : new_value for item in list}
# new_dict = {new_key : new_value for (key,value) in dict.items()}
import random
import pandas as pd
names = ["angela", "alex" , "yahir", "ana", "tony", "bahaa"]

student_scores = {student:random.randint(1,100) for student in names}

print(student_scores)

passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split(" ")}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {Day:(Temperature * 9/5) + 32 for (Day, Temperature) in weather_c.items()}

print(weather_f)

student_dic = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_dataframe = pd.DataFrame(student_dic)
print(student_dataframe)

for (index, row) in student_dataframe.iterrows():
    print(row.student)
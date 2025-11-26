'''
try:
    file = open("learningbasicpy/Day 30/file.txt")
    a_dict = {"key": "value"}
    #print(a_dict["sddadas"])

except FileNotFoundError:

    file = open("learningbasicpy/Day 30/file.txt", "w")
    file.write("some")

except KeyError as error_message:
    print(f"Wrong Key error:{error_message}")

else:
    content = file.read()
    print(f"content: {content}")

finally:
    raise KeyError("ERROR MINE")

'''

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height **2
print(bmi)
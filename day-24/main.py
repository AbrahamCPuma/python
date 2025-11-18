
with open("D:/python/learningbasicpy/day-24/my_new_file.txt") as file:
    contents = file.read()
    print(contents)

    with open("D:/python/learningbasicpy/day-24/my_new_file.txt",mode="a") as file:
        file.write("\nNew text 2")
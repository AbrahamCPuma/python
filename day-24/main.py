
with open("../../../new.txt") as file:
    contents = file.read()
    print(contents)

    with open("../../../new.txt",mode="a") as file:
        file.write("\nNew text 2")
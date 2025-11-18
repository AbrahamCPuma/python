
# TO-DO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PROJECT_PATH ="D:/python/learningbasicpy/Mail+Merge+Project+Start/Mail Merge Project Start/"

with open(f"{PROJECT_PATH}Input/Names/invited_names.txt") as names_files:
    names = names_files.readlines()
    print(names)

    
    

with open(f"{PROJECT_PATH}Input/Letters/starting_letter.txt",mode="r") as letter:
    content = letter.read()
    for name in names:
        name = name.strip("\n")
        name_switch = content.replace("[name]",f"{name}")
        with open(f"{PROJECT_PATH}Output/ReadyToSend.letter_for_{name}.txt",mode="w") as new_letter:
            new_letter.write(f"{name_switch}")

        print(f"\nCreated letter for {name}...")
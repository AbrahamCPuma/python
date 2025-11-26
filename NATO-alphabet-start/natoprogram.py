import pandas as pd

file_path = "D:/python/learningbasicpy/NATO-alphabet-start/"
df = pd.read_csv(f"{file_path}nato_phonetic_alphabet.csv")

nato_dic = {row.letter:row.code for (index, row) in df.iterrows()}

while True:
    word = input("Type a word: ").upper()

    try:
        nato_code = [nato_dic[n] for n in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")

    else:
        print(nato_code)
        break
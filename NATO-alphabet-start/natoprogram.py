import pandas as pd

file_path = "D:/python/learningbasicpy/NATO-alphabet-start/"
df = pd.read_csv(f"{file_path}nato_phonetic_alphabet.csv")

nato_dic = {row.letter:row.code for (index, row) in df.iterrows()}
print(nato_dic) 

word = input("Type a word: ").upper()

nato_code = [nato_dic[n] for n in word]
print(nato_code)